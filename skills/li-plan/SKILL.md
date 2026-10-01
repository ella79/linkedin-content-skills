---
name: li-plan
description: Plan the week. What to post, when to post it, and a short list of people to engage with. Rotates topics and hook formulas so nothing repeats. Writes plan.md. Reads voice.md.
---

# li-plan

The week on one page, so posting is a decision made once, not every morning.

## Method
- Cadence: 2-5 posts a week with at least 24h spacing (what LinkedIn data
  supports). Default Monday / Wednesday / Friday unless `voice.md` says otherwise.
- Rotate topics from `voice.md` and hook formulas from `li-human/hooks.json`; never
  repeat last week's thesis or hook.
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
