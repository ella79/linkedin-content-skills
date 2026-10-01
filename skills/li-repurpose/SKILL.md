---
name: li-repurpose
description: Turn one long asset (video, transcript, article, newsletter, call) into 4-6 LinkedIn posts that each stand alone. Extracts claims, numbers, stories and quotable lines first. Reads voice.md.
---

# li-repurpose

One source in, a week of posts out, each one able to stand on its own.

## Steps
1. The author pastes or links the asset (transcript, article, newsletter, notes).
2. **Extract before writing:** list the claims, real numbers, stories, mechanisms,
   mistakes and quotable lines, with counts. If the asset yields fewer than four
   distinct angles, say it is thin rather than padding.
3. For each angle, write a standalone post with `li-post`'s rules (hook, one idea,
   anchor, takeaway, CTA). No two posts may share a thesis or reuse a line.
4. Run `li-human` on each.

## Rules
- Each post must make sense to someone who never saw the source.
- Keep the author's voice (`~/.claude/linkedin/voice.md`); real anchors only.
- Spread them over days; note a suggested order.

## Output
4-6 copy-ready posts, each with its hook and a one-line note on the angle it
takes, plus a suggested posting order.
