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
