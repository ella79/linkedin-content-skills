#!/usr/bin/env python3
"""
card.py - render the image that goes with a post, at the size LinkedIn actually
rewards.

Sizes are not a style choice. Portrait 1080x1350 (4:5) takes the most screen on a
phone and carries the highest average engagement; square 1080x1080 is the middle
ground; 1200x627 is the link-preview ratio and wastes half a phone screen, so it
is offered only when something genuinely needs width.

Layouts exist so two posts never look alike:
  stat      one number carries the card
  quote     one sentence, set large
  terminal  real output from a file, rendered as a terminal window

Examples
  card.py --layout stat --kicker "PANGRAM STUDY" --stat "41%" \
          --line "of long-form LinkedIn posts are written by AI." \
          --sub "That isn't the problem. They all sound the same." --out card.png
  card.py --layout quote --line "Green is not the goal. Correct is." --out card.png
  card.py --layout terminal --file run.txt --kicker "BOTH GATES" --out card.png
"""
import argparse, os, sys
from PIL import Image, ImageDraw, ImageFont

SIZES = {"portrait": (1080, 1350), "square": (1080, 1080), "wide": (1200, 627)}

# A dark base reads well in feed and keeps text legible. Override with --accent
# so each post can carry its own temperature instead of one house style.
BG = (14, 19, 25)
WHITE = (230, 237, 243)
GREY = (139, 148, 158)
BORDER = (48, 54, 61)
ACCENTS = {"blue": (88, 166, 255), "green": (63, 185, 80), "orange": (240, 136, 62),
           "amber": (217, 164, 65), "violet": (165, 142, 255), "rose": (240, 110, 130)}

FD = "/usr/share/fonts/truetype/dejavu"
def font(name, size):
    path = {"r": f"{FD}/DejaVuSans.ttf", "b": f"{FD}/DejaVuSans-Bold.ttf",
            "m": f"{FD}/DejaVuSansMono.ttf", "mb": f"{FD}/DejaVuSansMono-Bold.ttf"}[name]
    return ImageFont.truetype(path, size)

def tracked(d, xy, text, f, fill, sp=2.5):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + sp

def wrap(d, text, f, maxw):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=f) <= maxw:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

def render(a):
    W, H = SIZES[a.size]
    acc = ACCENTS.get(a.accent, ACCENTS["blue"])
    im = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(im)
    M = int(W * 0.074)
    maxw = W - 2 * M

    if a.layout == "terminal":
        if not a.file or not os.path.exists(a.file):
            sys.exit("--layout terminal needs --file with the captured output")
        lines = [l for l in open(a.file, encoding="utf-8").read().splitlines()]
        fm, fmb = font("m", 17), font("mb", 17)
        y = M
        if a.kicker:
            tracked(d, (M, y), a.kicker.upper(), font("mb", 21), acc)
            y += 48
        d.rectangle([M - 14, y, W - M + 14, y + 44], fill=(22, 27, 34))
        for i, c in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
            d.ellipse([M + i * 26, y + 15, M + 14 + i * 26, y + 29], fill=c)
        y += 60
        for l in lines:
            if y > H - M - 70:
                break
            col = GREY if l.startswith("    ") else WHITE
            fnt = fm
            if l.strip().startswith("$"):
                col, fnt = acc, fmb
            elif any(k in l for k in ("PASS", "CARRIES", "[  ok  ]", "[ ok ]")):
                col, fnt = ACCENTS["green"], fmb
            elif set(l.strip()) <= set("=-") and l.strip():
                col = BORDER
            d.text((M, y), l, font=fnt, fill=col)
            y += 26

    elif a.layout == "stat":
        # measure the block first so it sits centred instead of stranding space
        fl_m = font("b", int(W * 0.041))
        fsub_m = font("r", int(W * 0.032))
        bh = (56 if a.kicker else 0) + int(W * 0.235)
        bh += len(wrap(d, a.line or "", fl_m, maxw)) * int(W * 0.054)
        if a.sub:
            bh += 54 + len(wrap(d, a.sub, fsub_m, maxw)) * int(W * 0.044)
        y = max(M + 10, (H - 70 - bh) // 2)
        if a.kicker:
            tracked(d, (M, y), a.kicker.upper(), font("mb", 24), acc)
            y += 56
        fs = font("b", int(W * 0.21))
        d.text((M, y), a.stat or "", font=fs, fill=acc)
        y += int(W * 0.235)
        fl = font("b", int(W * 0.041))
        for l in wrap(d, a.line or "", fl, maxw):
            d.text((M, y), l, font=fl, fill=WHITE)
            y += int(W * 0.054)
        if a.sub:
            y += 26
            d.line([M, y, W - M, y], fill=BORDER, width=2)
            y += 28
            fsub = font("r", int(W * 0.032))
            for l in wrap(d, a.sub, fsub, maxw):
                d.text((M, y), l, font=fsub, fill=GREY)
                y += int(W * 0.044)

    else:  # quote
        fq = font("b", int(W * 0.062))
        lines = wrap(d, a.line or "", fq, maxw)
        y = (H - len(lines) * int(W * 0.078)) // 2 - 40
        if a.kicker:
            tracked(d, (M, y - 70), a.kicker.upper(), font("mb", 23), acc)
        for l in lines:
            d.text((M, y), l, font=fq, fill=WHITE)
            y += int(W * 0.078)
        if a.sub:
            y += 24
            fsub = font("r", int(W * 0.032))
            for l in wrap(d, a.sub, fsub, maxw):
                d.text((M, y), l, font=fsub, fill=GREY)
                y += int(W * 0.044)

    if a.footer:
        d.line([M, H - M - 56, W - M, H - M - 56], fill=BORDER, width=2)
        d.text((M, H - M - 36), a.footer, font=font("mb", int(W * 0.023)), fill=acc)
    im.save(a.out, quality=95)
    print(f"{a.out}  {W}x{H}  layout={a.layout}  accent={a.accent}")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--layout", default="stat", choices=["stat", "quote", "terminal"])
    p.add_argument("--size", default="portrait", choices=list(SIZES))
    p.add_argument("--accent", default="blue", choices=list(ACCENTS))
    p.add_argument("--kicker"); p.add_argument("--stat"); p.add_argument("--line")
    p.add_argument("--sub"); p.add_argument("--footer"); p.add_argument("--file")
    p.add_argument("--out", default="card.png")
    render(p.parse_args())

if __name__ == "__main__":
    main()
