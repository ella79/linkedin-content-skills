---
name: li-plan
description: Plan the week. What to post, when to post it, and a short list of people to engage with. Rotates topics and hook formulas so nothing repeats. Writes plan.md. Reads voice.md.
---

# li-plan

The week on one page, so posting is a decision made once, not every morning.

## Method
- Cadence: 2-5 posts a week, never less than 4-6 hours apart and in practice a day
  apart. Three posts a week that land beat daily posts that do not. Default Monday /
  Wednesday / Friday unless `voice.md` says otherwise.
- **Hold a topic core.** The feed sorts an author into professional cohorts by topic,
  and consistency inside one area compounds into better distribution over time.
  Keep roughly 70% of the plan inside the author's two or three core topics and
  treat the rest of `voice.md`'s list as occasional. Rotating evenly across ten
  topics trains no cohort and costs reach.
- Rotate topics from `voice.md` and hook formulas from `li-human/hooks.json`.
  Read `~/.claude/linkedin/log.md` and rule out every thesis and hook formula used
  in the last ~10 posts, not just last week's.
- Each slot gets: the topic, the format (text / carousel / repurpose), the hook
  formula to try, and a one-line angle. Research happens when the post is written,
  not now.
- Add ~10 people/posts to engage with (see `li-engagers`), because reach comes
  from commenting as much as posting.

## Output
1. A week table: day, topic, format, hook formula, angle.
2. The engagement shortlist (who/what, why).
3. Write it to `~/.claude/linkedin/plan.md` so `li-audit` can check it later.
Never auto-post; each slot is still drafted and approved on its day.
