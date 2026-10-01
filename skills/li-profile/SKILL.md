---
name: li-profile
description: Score your LinkedIn profile against a 12-part rubric out of 100, then rewrite in fix-first order. Covers headline, about, banner, featured, experience and skills. Reads voice.md.
---

# li-profile

The profile is the landing page every post sends traffic to. This scores it and
rewrites the weak parts first.

## Inputs
The author pastes their current headline, About section, experience bullets, and
(optional) a description of the banner and Featured section.

## The 12-part rubric (score each 0-100, then average)
1. Headline - says what you do and for whom in the first 5 words, not a job title.
2. Hook line of About - earns the "see more" click.
3. About body - specific, first person, proof not adjectives.
4. Keywords - the terms a recruiter or client actually searches, present naturally.
5. Banner - states the positioning, not a stock photo.
6. Featured - the three things you want judged first.
7. Experience - outcomes and scope, not duties.
8. Skills - the ones your target roles screen on, ordered.
9. Proof - links, repos, talks, numbers you can stand behind.
10. Consistency - headline, About and posts tell one story.
11. Call to action - the reader knows the next step.
12. Voice - sounds like you (`~/.claude/linkedin/voice.md`), not a template.

## Output
1. The score per item and the average, with a one-line reason each.
2. Rewrites in **fix-first order** (lowest scores first): the current text vs the
   proposed text, so the author approves before changing anything.
3. Run `li-human` on every rewrite. No invented numbers.

## Hands off to
This is where the chain ends, after she approves the rewrites. If the audit later
shows a topic cohort forming, come back and align the headline with it.

## Preconditions
- Current headline, About and experience are pasted.

## Done when (verify, do not assume)
- All 12 rubric items scored with a one-line reason each, plus the average.
- Rewrites ordered lowest score first, not top to bottom.
- Every rewrite shown as current vs proposed, so she approves before anything changes.
- No invented numbers in any rewrite.
