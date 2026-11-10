# Fast Fleet – highlight / story templates (approved Nov 2026)

Flat, formal 9:16 (1080×1920) info slides and highlight covers. Run from this folder (needs Python, Playwright + Chromium, Pillow).

| File | What it builds | Output |
|---|---|---|
| `k_gen.py` then `shot_h.py` | "How to Book" slides (3 Arabic + 3 English). Also holds the shared CSS and helpers (`head`, `step`, `lst`, `one`, `contact`, `build`) | `out7/h*.png` |
| `q_gen.py` | FAQ slides (3 Arabic + 3 English), numbered with a gold circle under the headline; reuses `k_gen.py` helpers | `out9/final/faq_*.jpg` |
| `c_gen.py` | Highlight covers (line icon, matte gold #B08A1E on #0C0C0E) | `out8/final/cover_*.jpg` |

To add a slide: add one `build('name', head(title, subtitle) + cards + contact(1620))` line (pass `True` as last argument for English), keep cards between y=800 and y=1590, and re-run. Design rules live in the project doc `claude/design-rules.md`.
