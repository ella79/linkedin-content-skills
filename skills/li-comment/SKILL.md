---
name: li-comment
description: Write a comment on someone else's LinkedIn post that reads as a person with an opinion, not a bot. Picks the comment type from what the post actually says. Reads voice.md. Never "Great post!".
---

# li-comment

The author pastes the post text (never scrape the feed). You write a comment in
their voice (`~/.claude/linkedin/voice.md`) that adds something.

## Pick the type from the post
- Add a mechanism the post left out.
- Give a counter-case, respectfully, with a reason.
- Share a firsthand data point (from `story-bank.md`, real only).
- Ask one specific question only the author could answer.
- Extend the idea one step further.
- Name the trade-off the post skipped.
- Correct a factual slip, with a source, kindly.
- Tell a two-line real moment that matches.
- Agree and sharpen: restate the strongest version.

## Rules
- Never "Great post!", never generic praise, never emoji-only.
- One idea. Two to four sentences. Sound senior, not eager.
- If you have nothing true to add, say so; do not manufacture a take.
- Run `li-human` before delivering.

## Output
The comment, copy-ready, plus one shorter alternative.

## Hands off to
-> `li-engagers` for the next entry, if working through a list. Otherwise this is
where the chain ends: she pastes it herself.

## Preconditions
- The post being commented on is pasted. Never scraped from the feed.
- `voice.md` exists.

## Done when (verify, do not assume)
- The comment type was chosen from what the post actually says, and named.
- It adds a mechanism, a counter-case, a real data point or a specific question.
- Nothing generic: no "Great post", no praise-only, no emoji-only.
- If there was nothing true to add, that was said rather than manufactured.
