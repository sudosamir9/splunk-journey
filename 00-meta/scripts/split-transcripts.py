#!/usr/bin/env python3
"""
split-transcripts.py

Splits Saif Al-Shoker's monolithic course transcript into 68 separate
markdown files, one per lecture, organized into the 11 theme folders.

The input file uses these delimiters:
    === Section ===       (Saif's sections — ignored; we use our own themes)
    --- Lecture Title --- (one per lecture, 68 total)

Lecture kinds:
    - video    — normal lecture with a transcript
    - document — lecture with body "[No transcript available for this lecture]".
                 These are real lectures on Udemy (links/commands/resources),
                 just not video. The script preserves the marker and adds a
                 TODO so the user can paste content manually later.

Each output file:
    - Lives under <out-dir>/<theme>/NN-slug.md
    - Has YAML frontmatter (course, theme, lecture, title, kind, source)
    - Followed by either the raw transcript or a placeholder section

Usage:
    python3 split-transcripts.py <input.txt> [--out-dir DIR] [--dry-run]

Recommended workflow:
    1. Run in /tmp/ first to verify output
    2. Inspect a few files
    3. Move/copy to your repo's 02-course-saif/transcripts/
"""

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Theme mapping: lecture number → theme folder name
# ---------------------------------------------------------------------------
THEME_MAP = {
    range(1, 5):    "01-fundamentals",
    range(5, 17):   "02-install-bestpractices",
    range(17, 22):  "03-apps-configs-layering",
    range(22, 29):  "04-indexes-buckets",
    range(29, 31):  "05-users-ldap",
    range(31, 37):  "06-forwarders-distributed",
    range(37, 44):  "07-data-flow-concepts",
    range(44, 46):  "08-deployment-server",
    range(46, 54):  "09-data-inputs",
    range(54, 62):  "10-capstone-lab",
    range(62, 69):  "11-data-onboarding",
}

LECTURE_MARKER = re.compile(r"^---\s+(.+?)\s+---\s*$")
SECTION_MARKER = re.compile(r"^===\s+(.+?)\s+===\s*$")
NO_TRANSCRIPT_MARKER = "[No transcript available for this lecture]"


def theme_for(n: int) -> str:
    for r, theme in THEME_MAP.items():
        if n in r:
            return theme
    raise ValueError(f"No theme mapping for lecture {n}")


def slugify(title: str) -> str:
    """Lowercase, hyphens, alphanumerics + hyphens only, max ~60 chars."""
    s = title.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s[:60].rstrip("-")


def classify(body: str) -> str:
    """Return 'document' if the lecture is a non-video resource lecture, else 'video'."""
    return "document" if NO_TRANSCRIPT_MARKER in body else "video"


def parse_transcript(path: Path):
    """Yield (lecture_num, title, body) tuples in order."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    current_title = None
    current_body = []
    lecture_num = 0

    for line in lines:
        # Skip Saif's section headers — we use our own themes.
        if SECTION_MARKER.match(line):
            continue

        m = LECTURE_MARKER.match(line)
        if m:
            if current_title is not None:
                yield lecture_num, current_title, "\n".join(current_body).strip()
            lecture_num += 1
            current_title = m.group(1).strip()
            current_body = []
        else:
            if current_title is not None:
                current_body.append(line)

    if current_title is not None:
        yield lecture_num, current_title, "\n".join(current_body).strip()


def build_video_body(n: int, title: str, transcript: str) -> str:
    return (
        f"# Lecture {n} — {title}\n\n"
        "> Raw transcript. Notes go in `02-course-saif/notes/`, not here.\n\n"
        f"{transcript}\n"
    )


def build_document_body(n: int, title: str) -> str:
    """For document lectures: a clear placeholder the user fills in manually."""
    return (
        f"# Lecture {n} — {title}\n\n"
        "> **This is a document lecture, not a video.** On Udemy it contains "
        "links, commands, or written resources rather than a video transcript.\n\n"
        f"`{NO_TRANSCRIPT_MARKER}`\n\n"
        "---\n\n"
        "## TODO — paste content from Udemy\n\n"
        "<!-- Replace this section with the actual document contents from Udemy. "
        "Grep for `TODO — paste content` to find all document lectures still needing content. -->\n"
    )


def write_lecture(out_dir: Path, n: int, title: str, body: str, source_name: str, dry_run: bool):
    theme = theme_for(n)
    slug = slugify(title)
    filename = f"{n:02d}-{slug}.md"
    target = out_dir / theme / filename
    kind = classify(body)

    frontmatter = (
        "---\n"
        f"course: saif-admin\n"
        f"theme: {theme}\n"
        f"lecture: {n}\n"
        f'lecture-title: "{title}"\n'
        f"kind: {kind}\n"
        f'source: "{source_name}"\n'
        f"tags: [course/saif-admin, theme/{theme}, transcript, kind/{kind}]\n"
        "---\n\n"
    )

    if kind == "document":
        output = frontmatter + build_document_body(n, title)
    else:
        output = frontmatter + build_video_body(n, title, body)

    marker = "[DOC]" if kind == "document" else "     "
    if dry_run:
        print(f"  [dry] {marker} would write {target}  ({len(output):,} bytes)")
        return kind

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(output, encoding="utf-8")
    print(f"  {marker} wrote {target}  ({len(output):,} bytes)")
    return kind


def main():
    p = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    p.add_argument("input", type=Path, help="Path to the monolithic transcript .txt file")
    p.add_argument(
        "--out-dir",
        type=Path,
        default=Path("02-course-saif/transcripts"),
        help="Output base directory (default: 02-course-saif/transcripts/)",
    )
    p.add_argument("--dry-run", action="store_true", help="Show what would be written; don't write")
    args = p.parse_args()

    if not args.input.exists():
        print(f"ERROR: input file not found: {args.input}", file=sys.stderr)
        sys.exit(1)

    # Ensure theme subfolders exist (script creates them itself if missing).
    if not args.dry_run:
        args.out_dir.mkdir(parents=True, exist_ok=True)
        for theme in set(THEME_MAP.values()):
            (args.out_dir / theme).mkdir(parents=True, exist_ok=True)

    print(f"Reading {args.input}")
    print(f"Output: {args.out_dir}/<theme>/")
    print(f"Dry run: {args.dry_run}")
    print()

    count = 0
    doc_count = 0
    source_name = args.input.name
    doc_files = []

    for n, title, body in parse_transcript(args.input):
        kind = write_lecture(args.out_dir, n, title, body, source_name, args.dry_run)
        count += 1
        if kind == "document":
            doc_count += 1
            doc_files.append(f"  - lecture {n}: {title}")

    print()
    print(f"Processed {count} lectures total.")
    print(f"  Videos:    {count - doc_count}")
    print(f"  Documents: {doc_count}   (need manual content paste)")

    if doc_count:
        print()
        print("Document lectures to fill in manually:")
        for line in doc_files:
            print(line)

    if count != 68:
        print(
            f"\nWARNING: expected 68 lectures, got {count}. "
            "Inspect the source for missing/extra delimiters.",
            file=sys.stderr,
        )
        sys.exit(2)


if __name__ == "__main__":
    main()