---
name: li-card
description: Make the image that goes with a post, at the size LinkedIn actually rewards. Renders portrait 1080x1350 (4:5), square 1080x1080 or a terminal window from real output, with a different composition each time. Runs card.py. Use with every post that has an image.
---

# li-card

The image is not decoration. It decides how much of a phone screen the post
occupies, and screen time is dwell time, which is the heaviest ranking signal
the feed has.

## Size: documented, not a preference
| Size | Use | Why |
|---|---|---|
| **1080x1350 (4:5 portrait)** | the default | takes the most screen real estate and carries the highest average engagement rate |
| 1080x1080 (square) | one number, a quote, an announcement | larger than landscape, safer when the content is short |
| 1200x627 (landscape) | only when the content genuinely needs width | this is the **link-preview** ratio; as a feed upload it wastes half a phone screen |

Default to portrait. Reach for landscape only with a reason.

## Pick the composition from the post, not from a template
Run `card.py` with the layout that carries this particular idea:

- `--layout stat` - one number does the work. For research-backed posts.
- `--layout quote` - one sentence, set large. For a position or a principle.
- `--layout terminal` - real captured output rendered as a terminal window. For
  anything where the artefact is the proof. This is often the strongest option
  for a technical audience, because it cannot be faked by a designer.

Set the temperature with `--accent` (blue, green, orange, amber, violet, rose) to
match the subject. A warning post and a launch post should not feel the same.

**Never ship the same layout twice in a row.** Two near-identical images days
apart read as production, not as thinking. Consistency belongs in the writing.

## Run it
```
python3 ~/.claude/skills/li-card/card.py --layout stat --accent orange \
  --kicker "PANGRAM STUDY" --stat "41%" \
  --line "of long-form LinkedIn posts are written by AI." \
  --sub "That isn't the problem. They all sound like the same person." \
  --footer "github.com/you/your-repo" --out card.png
```
```
python3 ~/.claude/skills/li-card/card.py --layout terminal \
  --file run.txt --kicker "both gates, on this exact post" --out card.png
```

## Animated images
LinkedIn animates a GIF in the feed only while it stays **under 5MB and under
400 frames**. Past either limit it freezes to the first frame, which is worse
than a still. Keep the canvas at 4:5, use a small adaptive palette, and hold the
final frame so the end state is what people see when the loop rests.

An animation has to earn itself. A progress bar filling or a check list ticking
shows a mechanism; motion added for decoration just costs file size.

## Honesty
A designed card can read as marketing, and a technical reader discounts
marketing. When the post makes a claim that an artefact can prove, show the
artefact. The card is there to make the claim visible, not to dress it up.
