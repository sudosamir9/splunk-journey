# NotebookLM generation — settings & prompt templates

Reusable recipe for generating NBLM outputs from a topic's `enhanced.md`. Each topic folder also has a filled, copy-paste `nblm.md`; this file is the master template behind those.

**Workflow:** one NotebookLM notebook **per topic**. Upload that topic's `enhanced.md` (optionally `pre-class.md`) as the source, then generate the outputs below. Keep one growing **course-wide** notebook on the side (add each `enhanced.md` as you finish it) for cross-topic Q&A and big-picture review — not for podcasts.

Every prompt below is ~90% fixed (your profile, goal, tone) with two **[bracketed]** slots filled per topic: `[TOPIC NAME]` and `[KEY DISTINCTIONS / MUST-COVER POINTS]`.

---

## Which outputs are prompt-driven?

| Output | Prompt matters | Real lever |
|---|---|---|
| Podcast (Audio Overview) | ✅ a lot | the focus prompt below |
| Quiz / "Test me" | ✅ somewhat | focus prompt + the doc's *Questions to drill* |
| Flashcards | ⚠️ a little | the doc's *Key terms* section |
| Mind map | ❌ no prompt field | the doc's heading hierarchy |
| Infographic | ⚠️ minimal | the doc's structure/sections |

For mind map / flashcards / infographic the source structure does the work — that's why `enhanced.md` has dedicated *Key terms*, *Questions to drill*, and a clean heading hierarchy.

---

## 1. Podcast (Audio Overview)
**Settings:** Format = **Deep Dive** · Length = **Default** · Language = English.
(*Don't use **Long** — it runs ~45–60 min. Keep **Default** and steer the length via the closing line of the prompt.*)

```
This is a learning episode for an experienced security engineer who already uses Splunk
daily (strong at SPL and searching) and now wants to genuinely understand Splunk platform
administration — the architectural "why" and the practical "how", not surface facts. Skip
search syntax and analyst basics; assume the listener knows those.

Focus this episode on [TOPIC NAME]. Prioritize understanding and the trade-offs an admin
makes, not just definitions. Make sure to clearly explain [KEY DISTINCTIONS / MUST-COVER POINTS].

Keep it concrete — use worked examples from the material. Call out common misconceptions and
any legacy-vs-current terminology. Near the end, pose a few of the drill questions so the
listener can self-check. Energetic and conversational, but dense and precise — this is
learning, not entertainment. Aim for a thorough episode of roughly 25–30 minutes — go deep
enough to fill that, but don't pad or repeat.
```

## 2. Quiz / "Test me"
```
Generate challenging questions that test real, practical understanding of [TOPIC NAME] at an
administrator level. Mix straightforward recall with scenario / "which would you choose"
questions. Deliberately target the easily-confused points: [KEY DISTINCTIONS / MUST-COVER POINTS].
Assume I already know SPL — test platform/admin understanding, not search syntax. Explain why
each correct answer is right and why the others are wrong.
```

## 3. Flashcards
```
Make flashcards from the key terms and the must-know distinctions in this material on
[TOPIC NAME]. Front = term or scenario; back = a tight, precise definition or the rule.
Include "which component / which config file / index-time vs search-time" style cards where relevant.
```

## 4. Mind map & 5. Infographic
No useful prompt field — generated from the source. Just ensure the topic's `enhanced.md` is the (only) source so the map/infographic stays scoped to the topic.

---

## Per-topic emphasis guidance
- **Concept-heavy topics** → lean "Architectural Deep Dive": connections, trade-offs, the *why*.
- **Lab/procedure topics** → lean "Practical Workflow Guide": the procedure, the gotchas, what breaks and how to fix it (still end with a few self-check questions).
