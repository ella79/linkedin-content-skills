---
name: li-hooks
description: Take apart a post that did well - which of the 21 formulas it uses, how it is built, why it worked, a blank template for your topic, and which of its AI tells not to copy. Reads li-human/hooks.json.
---

# li-hooks

Reverse-engineer a winner so you can reuse the structure, not the words.

## Input
The author pastes a post (theirs or someone else's) that performed well.

## Teardown
1. **Formula** - which of the 21 in `li-human/hooks.json` the first line uses (or the
   closest match). Name it.
2. **Build** - how the post is structured line by line: hook, turn, body pattern,
   close, CTA.
3. **Why it worked** - the specific mechanism (tension, specificity, a real number,
   a contrarian claim), not "it was engaging".
4. **Blank template** - the same structure with slots, for the author's topic.
5. **Tells not to copy** - anything in it that reads as AI or as a formula visible
   from orbit; name them so the author avoids them.

## Rules
- Describe structure, never plagiarise wording. The template is slots, not text.
- Pull the formula names from `li-human/hooks.json` so they stay consistent with
  `li-post` and `li-plan`.

## Output
The five sections above, with the blank template ready to hand to `li-post`.

## Hands off to
-> `li-post`, carrying the blank template extracted from the teardown, plus the
list of tells not to copy. If the teardown was of her own post, also append the
finding to `~/.claude/linkedin/learned.md` so `li-plan` can prefer that formula.

## Preconditions
- The post being torn down is pasted.

## Done when (verify, do not assume)
- The formula is named from `li-human/hooks.json`, or the closest match is stated as such.
- The build is described line by line, and why it worked names a mechanism, not "it was engaging".
- The template is slots, never the original wording.
- The AI tells in it are named so they are not copied.
