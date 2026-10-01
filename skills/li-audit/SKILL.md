---
name: li-audit
description: Post-mortem on what you already published. Ranks posts by engagement rate and reach multiple, not raw impressions, finds what the winners share, and says what to stop. Reads log.md if present.
---

# li-audit

The account is the only honest evidence. This mode reads what actually happened,
not what should have worked.

## Inputs
- The author's analytics export, or reaction/comment counts for the last ~30 posts.
- `~/.claude/linkedin/log.md` if present (which hook formula each post used, topic,
  format, URL), written by the other skills after each publish.

## Method
- Rank by **engagement per impression** and **reach multiple**, never by raw
  impressions (big numbers hide weak posts).
- Find what the top quartile share: hook formula (`li-human/hooks.json`), topic,
  format (text/carousel), length, posting time.
- Find what the bottom quartile share. Say plainly what to stop doing.
- Separate signal from noise: one viral post is not a pattern.

## Output
1. The ranked table (post, eng. rate, reach multiple, hook formula, format).
2. What the winners share (3-5 concrete patterns).
3. What to stop (2-3 things), each with the evidence.
4. Next week's bet: the format/topic/hook to try more of.

## Preconditions
- Real numbers exist: an analytics export, or reaction and impression counts.
- Without them, stop and ask. A post-mortem on guessed data is worse than none.

## Done when (verify, do not assume)
- Ranked by engagement per impression and reach multiple, never raw impressions.
- Patterns are drawn from at least the top and bottom quartile, not one viral post.
- What to stop is stated plainly, each with the evidence behind it.
- Findings written back so `li-post` and `li-plan` can read them.
