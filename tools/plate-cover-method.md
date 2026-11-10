# Plate cover method (Fast Fleet photos) – saved 11 Nov 2026

Owner rule: every licence plate in our designs is replaced with the Fast Fleet brand plate (dark plate, gold wings logo) **exactly like the Defender photos**. A flat rounded rectangle placed on top of the photo looks painted-on and is NOT acceptable (owner feedback 11 Nov 2026 00:07).

## What "right" means
- The brand plate sits exactly on the real plate: same position, same size (only ~1px bigger to hide the white edge), same perspective/angle as the car.
- Dark body (almost black gradient), thin gold border (not thick), gold wings logo filling most of the plate height.
- Slightly softened to match the photo's sharpness, with a very soft contact shadow.
- Do the work on the ORIGINAL photo (not on an already-covered one). Never cover with an oversized shape.

## Procedure
1. Get the original photo (site API: https://api.ffl.ae/api/v1/cars?page=N -> images[].url).
2. Crop the plate area and zoom 8x with NEAREST; read the 4 corners of the real plate (clockwise from top-left).
3. Run `cover_plate(src, dst, quad, 'logo_t.png')` from `tools/plate_cover.py` (also in repo majdtuffi/ffl-media/tools/plate_cover.py).
4. Zoom the result 6x and check: no white fringe, no oversized plate, natural angle. Then use the photo in the design.
Escalade example (cars id 176): front photo 176_2.jpg quad [(427.8,468.3),(500.6,468.0),(500.6,488.3),(427.8,488.6)]; rear photo 176_3.jpg quad [(792.0,364.8),(853.5,365.5),(853.5,383.6),(792.0,383.6)].
Logo file: transparent PNG of the site logo (wings + FAST FLEET text), 'logo_t.png'.

## Code (tools/plate_cover.py)
```python
"""Fast Fleet plate cover: replace a car's licence plate with the brand plate (dark plate + gold wings logo).
Method (same look as the Defender photos): the plate is placed EXACTLY on the real plate (same size, same
perspective), not a flat rounded rectangle on top of the picture.

Usage:
    from plate_cover import cover_plate
    cover_plate('in.jpg', 'out.jpg', quad=[(TLx,TLy),(TRx,TRy),(BRx,BRy),(BLx,BLy)], logo='logo_t.png')

quad = the 4 corners of the REAL plate in the source photo (pixels), clockwise from top-left.
Find them by cropping the plate region and zooming 8x (NEAREST) before reading the corners.
"""
import numpy as np, cv2
from PIL import Image, ImageDraw, ImageFilter

S = 8  # supersampling

def _texture(tw, th, logo_path):
    t = Image.new('RGBA', (tw, th), (0, 0, 0, 0))
    # body: dark with soft vertical gradient
    body = Image.new('RGBA', (tw, th))
    px = body.load()
    for y in range(th):
        v = int(30 - 16 * y / th)           # 30 -> 14
        for x in range(tw):
            px[x, y] = (v, v, v + 2, 255)
    r = int(1.6 * S)
    m = Image.new('L', (tw, th), 0)
    ImageDraw.Draw(m).rounded_rectangle((0, 0, tw - 1, th - 1), radius=r, fill=255)
    t.paste(body, (0, 0), m)
    d = ImageDraw.Draw(t)
    ins = int(1.3 * S)
    d.rounded_rectangle((ins, ins, tw - 1 - ins, th - 1 - ins), radius=max(1, r - ins // 2),
                        outline=(217, 171, 47, 215), width=max(2, int(0.55 * S)))
    lg = Image.open(logo_path).convert('RGBA')
    lh = int(th * 0.78)
    lw = int(lg.width * lh / lg.height)
    if lw > tw * 0.8:
        lw = int(tw * 0.8); lh = int(lg.height * lw / lg.width)
    lg = lg.resize((lw, lh), Image.LANCZOS)
    t.alpha_composite(lg, ((tw - lw) // 2, (th - lh) // 2))
    return t

def cover_plate(src, dst, quad, logo, grow=1.3, blur=0.55):
    img = Image.open(src).convert('RGB')
    q = np.array(quad, dtype=np.float32)
    c = q.mean(axis=0)
    # grow the quad a little so the white plate's anti-aliased edge is fully hidden
    v = q - c
    n = np.linalg.norm(v, axis=1, keepdims=True)
    q = q + v / n * grow
    w = (np.linalg.norm(q[1] - q[0]) + np.linalg.norm(q[2] - q[3])) / 2
    h = (np.linalg.norm(q[3] - q[0]) + np.linalg.norm(q[2] - q[1])) / 2
    tw, th = int(w * S), int(h * S)
    tex = _texture(tw, th, logo)
    pad = 10
    x0, y0 = int(q[:, 0].min()) - pad, int(q[:, 1].min()) - pad
    x1, y1 = int(q[:, 0].max()) + pad, int(q[:, 1].max()) + pad
    W, H = (x1 - x0) * S, (y1 - y0) * S
    dst_pts = ((q - [x0, y0]) * S).astype(np.float32)
    src_pts = np.array([[0, 0], [tw, 0], [tw, th], [0, th]], dtype=np.float32)
    M = cv2.getPerspectiveTransform(src_pts, dst_pts)
    arr = np.array(tex).astype(np.float32)
    arr[..., :3] *= arr[..., 3:4] / 255.0            # premultiply
    warped = cv2.warpPerspective(arr, M, (W, H), flags=cv2.INTER_CUBIC)
    # match the photo's softness
    k = int(blur * S) * 2 + 1
    warped = cv2.GaussianBlur(warped, (k, k), blur * S)
    small = cv2.resize(warped, (x1 - x0, y1 - y0), interpolation=cv2.INTER_AREA)
    a = np.clip(small[..., 3:4] / 255.0, 0, 1)
    rgb = small[..., :3]
    base = np.array(img.crop((x0, y0, x1, y1))).astype(np.float32)
    out = base * (1 - a) + rgb                          # premultiplied composite
    # very soft contact shadow around the plate
    sh = cv2.GaussianBlur(a, (0, 0), 1.6)[..., None] if a.ndim == 2 else cv2.GaussianBlur(a[..., 0], (0, 0), 1.6)[..., None]
    out = out * (1 - 0.25 * np.clip(sh - a, 0, 1))
    img.paste(Image.fromarray(np.clip(out, 0, 255).astype(np.uint8)), (x0, y0))
    img.save(dst, quality=95)
    return dst
```
