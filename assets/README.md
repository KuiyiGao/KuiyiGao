# assets/

Figures shown on the profile README. Keep this folder small — GitHub renders these
inline on the profile page, so weight and legibility matter more than resolution.

| Rule | Why |
|---|---|
| **PNG, 1200–1600 px wide, under 300 KB each** | three of them load on every profile view |
| **Readable at 400 px wide** | that is the real rendered width in a three-column table |
| **No text smaller than ~14 px in the source figure** | it becomes unreadable at a third width |
| **Light-neutral or transparent background** | GitHub shows the README on both light and dark themes; a white-background figure looks like a hole in dark mode. Prefer a transparent PNG with dark-grey ink, or supply both `-light.png` and `-dark.png` and use the `<picture>` element |
| **One idea per figure** | a full multi-panel paper figure is unreadable at this size — crop the one panel that carries the claim |
| **Name by claim, not by number** | `fig-recall-factorization.png`, not `figure3.png` |

Suggested first three (the claims worth showing to someone who has 20 seconds):

1. `fig-recall-factorization.png` — the three-factor decomposition of detector recall.
2. `fig-skill-firewall.png` — the firewall's data path: skill → proxy → intent/action/result check → decision + evidence.
3. `fig-noise-trajectories.png` — one before/after trajectory pair showing that noise changes *which* actions an agent takes.

Then uncomment the figure strip in `../README.md`.

## What is here now (2026-09-12)

One figure per project, all 1600×1000 so they tile evenly as thumbnails on the homepage. Every number inside a figure comes from a source that can be checked; nothing else is allowed in.

| File | Claim it carries | Where the numbers come from |
|---|---|---|
| `fig-mmsafeaware-two-failures.png` | safety awareness fails two ways: missing split intent, over-refusing benign input | arXiv 2502.11184 abstract — 1,500 pairs, 29 scenarios, nine MLLMs, GPT-4V 36.1% / 59.9%, three mitigations |
| `fig-chain-of-jailbreak.png` | one harmful request becomes a chain of harmless edits | arXiv 2410.03869 abstract — 9 × 3 × 3 CoJ-Bench, four services, >60% vs 14%, Think Twice >95% |
| `fig-gui-agent-interface-noise.png` | noise changes what the agent does, not only whether it succeeds | no numbers on purpose (paper under review); the three axes are from the abstract |
| `fig-skill-firewall.png` | pipeline + PASS/DEFER/BLOCK, then the reach-the-check measurement | repo; 0/65 and 46/65 from the measurement study (manuscript in preparation) |
| `fig-memslot-pipeline.png` | decide what matters before the question is asked | repo README — frozen RoBERTa, 32 slots, 64–400 vision tokens, CUAD metrics, ten arms; the page crop is the project's own `distorted_rendering.png` (rendering primitive) |
| `fig-movability-segmentation.jpg` | which pixels can move — a perception prior | course report — mIoU 0.6381, 58.21 FPS, Table 1 level names; tiles are the report's epoch-50 predictions |
| `fig-recall-factorization.png` | recall = P(execute)·P(observe\|execute)·P(detect\|observed) | kept for the measurement paper; not currently shown |

Regenerate: `python3 _source/mkfigs.py` writes SVGs to `out/`; render at a 1600×1000 viewport (Playwright/Chromium) and quantize schematic ones to 128 colours. The two raster figures need `src/mov-*.png` (cropped from the report PDF) and `src/ocr-crop.png` (cropped from the repo's rendering).
