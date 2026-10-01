---
name: li-engagers
description: Build a short list of the people and posts worth engaging with this week, with a reason and an angle for each. Reach comes from commenting as much as posting. Reads voice.md. You paste candidates; never scrape.
---

# li-engagers

Posting is half of it. The other half is showing up, with substance, where your
audience already is. This builds the shortlist.

## Inputs
The author pastes candidate posts or names (from their feed, their field, people
they want on their radar). Never scrape the feed.

## Method
- Pick ~10 worth a real comment this week, biased toward:
  - people your target readers already follow,
  - posts where you have a genuine, specific thing to add,
  - adjacent voices (not just the giants, who rarely reply).
- For each: the reason to engage, and the angle (which `li-comment` type fits).
- Skip anything where you would have to fake interest.

## Output
A table: who/what, why them, the comment angle. Hand each row to `li-comment`
when it is time to write. Spread them across the week; feed `li-plan`.
