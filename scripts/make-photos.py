# -*- coding: utf-8 -*-
"""從原檔重新產生站上用的照片。改裁切就改這裡的參數，然後重跑：

    python3 scripts/make-photos.py

原檔：侯律師照片.jpg（2000×1334 橫幅，家屬 2026-09-07 提供，事務所書櫃前）
產出：public/images/hou-portrait.jpg   4:5 直幅 1040×1300，index／profile 兩處共用
      public/images/og.jpg            1200×630，分享到 LINE／Facebook 的預覽圖
需要 Pillow：pip3 install Pillow
"""
from PIL import Image, ImageDraw, ImageFont
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, '侯律師照片.jpg')
OUT = os.path.join(ROOT, 'public', 'images')

# 直幅裁切參數：CROP_H 越小＝裁越緊；CENTER_X 是人物在原檔的水平中心。
CROP_H, CENTER_X = 1160, 900          # 1334 全高太鬆、1000 會切到手臂
SONGTI = '/System/Library/Fonts/Supplemental/Songti.ttc'   # 索引 7=TC Regular、2=TC Bold
GOLD, CREAM = (201, 168, 112), (247, 244, 237)


def font(size, bold=False):
    return ImageFont.truetype(SONGTI, size, index=2 if bold else 7)


def gradient(size, start, end, horiz=False):
    """畫一條線性漸層後拉滿整張圖。horiz=True 為左右向，否則上下向。"""
    w, h = size
    n = w if horiz else h
    strip = Image.new('RGB', (w, 1) if horiz else (1, h))
    px = strip.load()
    for i in range(n):
        t = i / (n - 1)
        c = tuple(int(start[k] + (end[k] - start[k]) * t) for k in range(3))
        if horiz:
            px[i, 0] = c
        else:
            px[0, i] = c
    return strip.resize(size, Image.BILINEAR)


def tracked(draw, xy, text, fnt, fill, track=0):
    """逐字加字距——中文標題不加字距會太擠。"""
    x, y = xy
    for ch in text:
        draw.text((x, y), ch, font=fnt, fill=fill)
        x += draw.textlength(ch, font=fnt) + track


def main():
    os.makedirs(OUT, exist_ok=True)
    src = Image.open(SRC).convert('RGB')
    sw, sh = src.size

    cw = int(CROP_H * 0.8)
    x0 = max(0, min(sw - cw, CENTER_X - cw // 2))
    (src.crop((x0, 0, x0 + cw, CROP_H))
        .resize((1040, 1300), Image.LANCZOS)
        .save(os.path.join(OUT, 'hou-portrait.jpg'), quality=86, optimize=True, progressive=True))

    # OG 卡：深綠底，右側照片往左淡出，左側放姓名與事務所
    ow, oh, pw = 1200, 630, 520
    panel = src.crop((int(sw * 0.30), 0, int(sw * 0.30) + int(sh * pw / oh), sh))
    panel = panel.resize((pw, oh), Image.LANCZOS).convert('RGBA')
    mask = gradient((pw, oh), (0, 0, 0), (255, 255, 255), horiz=True).convert('L')
    panel.putalpha(mask.point(lambda v: min(255, int(v * 2.2))))

    card = gradient((ow, oh), (24, 56, 48), (13, 29, 25)).convert('RGBA')
    card.alpha_composite(panel, (ow - pw, 0))
    d = ImageDraw.Draw(card)
    tracked(d, (88, 150), '臺南 · 中西區府前路', font(24), GOLD, 6)
    d.line([(88, 214), (144, 214)], fill=GOLD, width=2)
    tracked(d, (88, 258), '侯明正律師', font(76, True), CREAM, 10)
    tracked(d, (88, 382), '侯明正律師事務所', font(30), (200, 206, 201), 5)
    tracked(d, (88, 452), '初次諮詢不收費 · 可電話或視訊', font(24), (168, 180, 172), 4)
    card.convert('RGB').save(os.path.join(OUT, 'og.jpg'), quality=88, optimize=True, progressive=True)
    print('寫出 hou-portrait.jpg 與 og.jpg 到', OUT)


if __name__ == '__main__':
    main()
