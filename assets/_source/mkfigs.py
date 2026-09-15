#!/usr/bin/env python3
"""Generate the six project figures as SVG (1600x1000), matching the style of
assets/fig-skill-firewall.png. Every number that appears here is tagged in
FIGURE_SOURCES below; nothing else is allowed in."""
import base64, io, os
from PIL import Image

W, H = 1600, 1000
FONT = "Liberation Sans, Arial, Helvetica, sans-serif"
INK, INK2, MUTED, LINE = "#1a1d21", "#3d4450", "#6b7280", "#c9d1dc"
BOX, BOX_S = "#eef1f5", "#c9d1dc"
AMB, AMB_S, AMB_T = "#fdf3dc", "#e2c27a", "#8a5a00"
GRN, GRN_S, GRN_T = "#eaf5ec", "#9fcfae", "#2b7a3b"
RED, RED_S, RED_T = "#fdeeee", "#e5a3a6", "#b4232a"
BLU, BLU_S, BLU_T = "#e8f0fb", "#9db9e3", "#1f4e8c"
ARROW = "#8a8f98"

FIGURE_SOURCES = {
 "fig-mmsafeaware-two-failures": "arXiv 2502.11184 abstract: 29 scenarios, 1500 pairs, nine MLLMs, GPT-4V 36.1% / 59.9%, three methods",
 "fig-chain-of-jailbreak": "arXiv 2410.03869 abstract: 9 scenarios x 3 edit ops x 3 editing elements, four services, >60% vs 14%, Think Twice >95%",
 "fig-gui-agent-interface-noise": "no numbers (under review); reliability / safety / trajectory from evidence base E3",
 "fig-skill-firewall": "E4: pipeline; 0/65 flagged, 46/65 no proxy-visible egress (own iclr/results, manuscript in preparation)",
 "fig-memslot-pipeline": "E6 + repo README: frozen RoBERTa, 32 MemSlots, 64-400 vision tokens, CUAD metrics EM/F1/AUPR/P@80%R, ten control arms; rendering crop from cuad_distorted_rendering/distorted_rendering.png (rendering primitive)",
 "fig-movability-segmentation": "E7 / report-2.pdf: mIoU 0.6381, 58.21 FPS, Table 1 level names; tiles from report Figure 5 (epoch 50)",
}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def text(x, y, s, size=26, weight=400, fill=INK, anchor="start", family=FONT, extra=""):
    return f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>'

def box(x, y, w, h, fill=BOX, stroke=BOX_S, r=14, sw=2):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def arrow(x1, y1, x2, y2, color=ARROW, sw=5):
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}" marker-end="url(#ah)"/>'

def img(path, x, y, w, h, r=10):
    b = base64.b64encode(open(path, "rb").read()).decode()
    cid = os.path.basename(path).replace(".", "-")
    return (f'<clipPath id="c-{cid}"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}"/></clipPath>'
            f'<image href="data:image/png;base64,{b}" x="{x}" y="{y}" width="{w}" height="{h}" preserveAspectRatio="xMidYMid slice" clip-path="url(#c-{cid})"/>'
            f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="none" stroke="{LINE}" stroke-width="2"/>')

def head(title, sub):
    return text(40, 74, title, 46, 700) + text(40, 122, sub, 26, 400, MUTED)

def wrap(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
            f'<defs><marker id="ah" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto" markerUnits="userSpaceOnUse">'
            f'<path d="M0,0 L12,6 L0,12 z" fill="{ARROW}"/></marker></defs>'
            f'<rect width="{W}" height="{H}" fill="#ffffff"/>' + body + '</svg>')

def verdict(x, y, w, h, label, kind):
    f, s, t = {"ok": (GRN, GRN_S, GRN_T), "bad": (RED, RED_S, RED_T), "amb": (AMB, AMB_S, AMB_T)}[kind]
    return box(x, y, w, h, f, s, 12, 3) + text(x + w / 2, y + h / 2 + 11, label, 30, 700, t, "middle")

def photo_glyph(x, y, w, h):
    # a generic "image" pictogram: frame + sun + mountains
    return (box(x, y, w, h, "#f7f8fa", BOX_S, 10, 2) +
            f'<circle cx="{x + w * 0.3}" cy="{y + h * 0.32}" r="{h * 0.11}" fill="{AMB_S}"/>'
            f'<path d="M{x + 8},{y + h - 8} L{x + w * 0.38},{y + h * 0.5} L{x + w * 0.58},{y + h * 0.76} L{x + w * 0.72},{y + h * 0.6} L{x + w - 8},{y + h - 8} z" fill="{BOX_S}"/>')

def text_glyph(x, y, w, h, lines=3):
    out = box(x, y, w, h, "#f7f8fa", BOX_S, 10, 2)
    for i in range(lines):
        ln = w - 28 if i < lines - 1 else (w - 28) * 0.6
        out += f'<rect x="{x + 14}" y="{y + 16 + i * (h - 24) / lines}" width="{ln}" height="8" rx="4" fill="{BOX_S}"/>'
    return out

def bar(x, y, w, h, frac, label_left, value, fill, stroke, tcol):
    out = box(x, y, w, h, "#f7f8fa", LINE, 10, 2)
    out += f'<rect x="{x}" y="{y}" width="{max(6, w * frac)}" height="{h}" rx="10" fill="{fill}" stroke="{stroke}" stroke-width="2"/>'
    out += text(x + 20, y + h / 2 + 10, label_left, 26, 500, INK2)
    out += text(x + w - 20, y + h / 2 + 13, value, 38, 700, tcol, "end")
    return out

# ---------------------------------------------------------------- F1
def f1():
    b = head("Safety awareness has two failure modes",
             "MMSafeAware · 1,500 image–prompt pairs · 29 safety scenarios · nine multimodal LLMs evaluated")
    for col, (cx, title, tag, verdict_lbl, sub) in enumerate([
        (40, "Unsafe pair", "unsafe only in combination", "“safe”  ✗", "the model misses split intent"),
        (820, "Benign pair", "harmless, looks edgy", "“unsafe”  ✗", "the model over-refuses")]):
        b += text(cx, 190, title, 32, 700)
        b += photo_glyph(cx, 215, 220, 150) + text(cx + 110, 395, "image", 22, 400, MUTED, "middle")
        b += text(cx + 232, 300, "+", 40, 400, MUTED)
        b += text_glyph(cx + 262, 215, 220, 150) + text(cx + 372, 395, "prompt", 22, 400, MUTED, "middle")
        b += f'<path d="M{cx},{412} L{cx},{424} L{cx + 482},{424} L{cx + 482},{412}" fill="none" stroke="{LINE}" stroke-width="2"/>'
        b += text(cx + 241, 452, tag, 22, 400, INK2, "middle")
        b += arrow(cx + 500, 290, cx + 560, 290)
        b += box(cx + 570, 250, 150, 80, BOX, BOX_S, 12, 2) + text(cx + 645, 300, "MLLM", 28, 700, INK, "middle")
        b += verdict(cx + 570, 350, 150, 70, verdict_lbl, "bad")
        b += text(cx + 645, 455, sub, 22, 400, RED_T, "middle")
    # bars
    b += text(40, 560, "GPT-4V on the benchmark", 26, 700, INK2)
    b += bar(40, 585, 1520, 92, 0.361, "unsafe inputs it calls safe", "36.1%", RED, RED_S, RED_T)
    b += bar(40, 695, 1520, 92, 0.599, "benign inputs it calls unsafe", "59.9%", AMB, AMB_S, AMB_T)
    b += box(40, 830, 1520, 120, "#f6f8fa", LINE, 14, 2)
    b += text(70, 878, "The benchmark scores both failures separately. Three mitigations were then tested — prompting, visual", 26, 400, INK2)
    b += text(70, 916, "contrastive decoding, and vision-centric reasoning fine-tuning — and none closed the gap.", 26, 400, INK2)
    return wrap(b)

# ---------------------------------------------------------------- F2
def canvas_glyph(x, y, w, h, stage):
    out = box(x, y, w, h, "#f7f8fa", BOX_S, 10, 2)
    if stage >= 1:
        out += f'<rect x="{x + w * 0.2}" y="{y + h * 0.35}" width="{w * 0.6}" height="{h * 0.45}" rx="8" fill="{BOX_S}"/>'
    if stage >= 2:
        out += f'<circle cx="{x + w * 0.5}" cy="{y + h * 0.3}" r="{h * 0.14}" fill="{AMB_S}"/>'
    if stage >= 3:
        out += f'<rect x="{x + w * 0.3}" y="{y + h * 0.5}" width="{w * 0.4}" height="{h * 0.14}" rx="6" fill="{RED_S}"/>'
    return out

def f2():
    b = head("One harmful request, split into a chain of harmless edits",
             "Chain-of-Jailbreak · CoJ-Bench: 9 safety scenarios × 3 editing operations × 3 editing elements · four image-generation services")
    # row 1: single prompt refused
    b += text(40, 190, "As a single prompt", 28, 700, INK2)
    b += box(40, 210, 420, 90, BOX, BOX_S, 12, 2) + text(250, 265, "harmful request", 28, 500, INK, "middle")
    b += arrow(470, 255, 540, 255)
    b += box(550, 210, 200, 90, BOX, BOX_S, 12, 2) + text(650, 265, "safeguard", 28, 500, INK, "middle")
    b += arrow(760, 255, 830, 255)
    b += verdict(840, 210, 200, 90, "refused", "ok")
    # row 2: chain
    b += text(40, 380, "As a chain of edits", 28, 700, INK2)
    xs = [40, 430, 820]
    labels = ["step 1 · generate", "step 2 · edit", "step 3 · edit"]
    for i, x in enumerate(xs):
        b += box(x, 400, 330, 210, BOX, BOX_S, 14, 2)
        b += text(x + 165, 440, labels[i], 26, 700, INK, "middle")
        b += canvas_glyph(x + 40, 455, 130, 130, i + 1)
        b += verdict(x + 190, 500, 120, 56, "passes", "ok")
        if i < 2:
            b += arrow(x + 340, 505, x + 420, 505)
    b += arrow(1160, 505, 1240, 505)
    b += box(1250, 400, 310, 210, RED, RED_S, 14, 3)
    b += text(1405, 470, "composed result", 26, 700, RED_T, "middle")
    b += text(1405, 515, "harmful", 36, 700, RED_T, "middle")
    b += text(1405, 570, "no single step was refusable", 20, 400, RED_T, "middle")
    # bars
    b += text(40, 690, "Bypass rate across the four services", 26, 700, INK2)
    b += bar(40, 712, 990, 78, 0.60, "Chain-of-Jailbreak", "> 60%", RED, RED_S, RED_T)
    b += bar(40, 806, 990, 78, 0.14, "prior jailbreak methods", "14%", BOX, BOX_S, INK2)
    b += box(1060, 712, 500, 172, GRN, GRN_S, 14, 3)
    b += text(1310, 760, "Think Twice Prompting", 26, 700, GRN_T, "middle")
    b += text(1310, 822, "> 95%", 54, 700, GRN_T, "middle")
    b += text(1310, 862, "of attacks defended", 22, 400, GRN_T, "middle")
    b += text(40, 940, "I designed the attack methodology, ran most of the attack and defense experiments, and wrote the paper.", 24, 400, MUTED)
    return wrap(b)

# ---------------------------------------------------------------- F3
def window(x, y, w, h, title):
    out = box(x, y, w, h, "#fbfbfc", BOX_S, 14, 2)
    out += f'<rect x="{x}" y="{y}" width="{w}" height="44" rx="14" fill="{BOX}"/>'
    out += f'<rect x="{x}" y="{y + 30}" width="{w}" height="14" fill="{BOX}"/>'
    for i, c in enumerate(["#e0a3a3", "#e3c88f", "#a7cfa9"]):
        out += f'<circle cx="{x + 24 + i * 24}" cy="{y + 22}" r="7" fill="{c}"/>'
    out += text(x + w / 2, y + 30, title, 22, 500, MUTED, "middle")
    return out

def ui_rows(x, y, w, n, shift=0):
    out = ""
    for i in range(n):
        yy = y + i * 46 + shift
        out += f'<rect x="{x}" y="{yy}" width="{w * (0.55 if i % 2 else 0.8)}" height="14" rx="7" fill="{LINE}"/>'
    return out

def path(points, color, dashed=False):
    d = " ".join(f"{'M' if i == 0 else 'L'}{px},{py}" for i, (px, py) in enumerate(points))
    dash = ' stroke-dasharray="14 10"' if dashed else ""
    out = f'<path d="{d}" fill="none" stroke="{color}" stroke-width="6" stroke-linejoin="round"{dash}/>'
    for i, (px, py) in enumerate(points):
        out += f'<circle cx="{px}" cy="{py}" r="12" fill="#fff" stroke="{color}" stroke-width="5"/>'
        out += f'<text x="{px}" y="{py + 6}" font-family="{FONT}" font-size="16" font-weight="700" fill="{color}" text-anchor="middle">{i + 1}</text>'
    return out

def f3():
    b = head("Interface noise changes what the agent does",
             "not only whether it succeeds · a cross-platform GUI-agent robustness benchmark · co-first author · under review")
    # clean window
    b += window(40, 170, 720, 560, "clean interface")
    b += ui_rows(80, 250, 640, 9)
    b += box(560, 620, 160, 60, BLU, BLU_S, 10, 2) + text(578, 658, "Submit", 24, 600, BLU_T)
    b += path([(120, 262), (120, 400), (400, 492), (692, 650)], BLU_T)
    b += text(400, 780, "same task · same agent · same goal", 24, 400, MUTED, "middle")
    b += verdict(40, 800, 720, 70, "reaches the goal", "ok")
    # noisy window
    b += window(840, 170, 720, 560, "noisy interface")
    b += ui_rows(880, 250, 640, 9, shift=36)   # content shifted by dynamic loading
    # overlay banner
    b += box(900, 300, 600, 110, AMB, AMB_S, 12, 3)
    b += text(1200, 345, "overlay / pop-up", 24, 700, AMB_T, "middle")
    b += text(1200, 383, "covers the element the agent expected", 20, 400, AMB_T, "middle")
    # deceptive widget
    b += box(1160, 620, 180, 60, RED, RED_S, 10, 3) + text(1178, 658, "Submit", 24, 600, RED_T)
    b += text(1250, 700, "deceptive widget", 18, 400, RED_T, "middle")
    b += box(1360, 620, 160, 60, BLU, BLU_S, 10, 2) + text(1440, 658, "Submit", 24, 600, BLU_T, "middle")
    b += path([(920, 262), (920, 430), (1100, 470), (1306, 650)], RED_T, dashed=True)
    b += text(1200, 780, "overlay · shifted content · look-alike control", 24, 400, MUTED, "middle")
    b += verdict(840, 800, 720, 70, "different action taken — sometimes an unsafe one", "bad")
    # footer
    b += text(40, 930, "Measured on three axes:", 24, 700, INK2)
    for i, t in enumerate(["reliability", "safety", "trajectory"]):
        b += box(330 + i * 230, 900, 210, 48, BOX, BOX_S, 24, 2) + text(435 + i * 230, 932, t, 24, 500, INK, "middle")
    b += text(1060, 932, "lower success · shifted action path · more unsafe actions", 22, 400, MUTED)
    return wrap(b)

# ---------------------------------------------------------------- F4
def f4():
    b = head("Agent Skill Firewall — runtime verification of agent skills",
             "Each PASS / DEFER / BLOCK verdict is recorded together with the evidence it was derived from")
    stages = [("Skill bundle", "manifest + code", BOX, BOX_S, INK),
              ("Static pre-scan", "declared intent", BOX, BOX_S, INK),
              ("Canary-seeded proxy", "observed action + result", AMB, AMB_S, AMB_T),
              ("intent vs action vs result", "verdict + evidence record", BOX, BOX_S, INK)]
    x = 40
    for i, (t, s, f, st, tc) in enumerate(stages):
        w = 320 if i < 3 else 380
        b += box(x, 190, w, 150, f, st, 16, 2)
        b += text(x + 24, 250, t, 28, 700, tc)
        b += text(x + 24, 300, s, 24, 400, tc if tc != INK else INK2)
        if i < 3:
            b += arrow(x + w + 8, 265, x + w + 52, 265)
        x += w + 60
    b += arrow(1370, 350, 1370, 410)
    b += verdict(760, 420, 240, 90, "PASS", "ok")
    b += verdict(1030, 420, 240, 90, "DEFER", "amb")
    b += verdict(1300, 420, 260, 90, "BLOCK", "bad")
    # measurement band
    b += box(40, 570, 1520, 380, "#f6f8fa", LINE, 16, 2)
    b += text(70, 625, "Then I measured whether the check is reached at all", 30, 700, INK2)
    b += text(70, 672, "on stored runs of 65 malicious agent skills:", 26, 400, INK2)
    b += bar(70, 700, 700, 84, 46 / 65, "produced no proxy-visible egress", "46 / 65", AMB, AMB_S, AMB_T)
    b += bar(70, 800, 700, 84, 0.0, "flagged by the runtime detector", "0 / 65", RED, RED_S, RED_T)
    b += box(820, 700, 710, 184, "#fff", LINE, 14, 2)
    b += text(1175, 750, "reported recall factors as", 24, 400, MUTED, "middle")
    b += text(1175, 800, "P(execute) · P(observe | execute) · P(detect | observed)", 26, 700, INK, "middle")
    b += text(1175, 850, "most of the loss is in the middle term", 24, 400, AMB_T, "middle")
    b += text(70, 925, "Built with a four-student team at MBZUAI UGRIP 2026 — I built the runtime firewall; the measurement study is a manuscript in preparation.", 22, 400, MUTED)
    return wrap(b)

# ---------------------------------------------------------------- F5
def f5():
    b = head("Decide what matters before the question is asked",
             "MemSlot saliency → distorted rendering → OCR vision tokens · long CUAD legal contracts")
    steps = [("Contract text", "held-out CUAD contract", BOX, BOX_S, INK),
             ("Frozen RoBERTa + 32 memory slots", "cross-attention learns question-agnostic saliency", BLU, BLU_S, BLU_T),
             ("Distorted rendering", "word size and colour encode importance", AMB, AMB_S, AMB_T),
             ("DeepSeek-OCR vision encoder", "the page becomes 64–400 vision tokens", BOX, BOX_S, INK),
             ("QA reader · CUAD-official metrics", "EM · F1 · AUPR · precision @ 80% recall", BOX, BOX_S, INK)]
    y = 175
    for i, (t, s, f, st, tc) in enumerate(steps):
        b += box(40, y, 760, 112, f, st, 14, 2)
        b += text(68, y + 46, t, 28, 700, tc)
        b += text(68, y + 86, s, 22, 400, tc if tc != INK else INK2)
        if i < len(steps) - 1:
            b += arrow(420, y + 118, 420, y + 150)
        y += 154
    b += img("src/ocr-crop.png", 850, 175, 710, 740, 12).replace('preserveAspectRatio="xMidYMid slice"', 'preserveAspectRatio="xMinYMin slice"')
    b += f'<rect x="852" y="862" width="706" height="51" fill="#ffffff" fill-opacity="0.92"/>'
    b += text(1205, 896, "a saliency-distorted page — larger and redder means more important", 22, 400, INK2, "middle")
    b += text(40, 955, "Leakage-free by construction: saliency is trained on train-split text only — no questions, no labels.", 22, 400, INK2)
    b += text(40, 985, "Compared against ten control arms (pruning, summarization, OCR-only) on the same reader.", 22, 400, INK2)
    return wrap(b)

# ---------------------------------------------------------------- F6
def f6():
    b = head("Which pixels can move? A perception prior for embodied safety",
             "COCO-Stuff relabelled into four movability levels · DeepLabV3 with a custom ASPP head · predictions after 50 epochs")
    tiles = ["street", "truck", "dinner", "bikes"]
    for i, t in enumerate(tiles):
        x = 40 + (i % 2) * 372
        y = 170 + (i // 2) * 372
        b += img(f"src/mov-{t}.png", x, y, 352, 352, 12)
    levels = [("3", "Highly mobile", "people, vehicles, animals", BOX, BOX_S, INK),
              ("2", "Inactively mobile", "clothes, food, small objects", BOX, BOX_S, INK),
              ("1", "Normally stable", "furniture, appliances, street facilities", BOX, BOX_S, INK),
              ("0", "Not movable", "buildings, landscape, plantation", BOX, BOX_S, INK)]
    y = 170
    for n, t, s, f, st, tc in levels:
        b += box(820, y, 740, 96, f, st, 14, 2)
        b += text(858, y + 62, n, 44, 700, tc)
        b += text(920, y + 42, t, 28, 700, tc)
        b += text(920, y + 78, s, 22, 400, INK2)
        y += 112
    b += box(820, 640, 355, 150, "#f6f8fa", LINE, 14, 2)
    b += text(997, 700, "0.638", 56, 700, INK, "middle")
    b += text(997, 745, "best mIoU on validation", 22, 400, MUTED, "middle")
    b += box(1205, 640, 355, 150, "#f6f8fa", LINE, 14, 2)
    b += text(1382, 700, "58 FPS", 56, 700, INK, "middle")
    b += text(1382, 745, "average inference speed", 22, 400, MUTED, "middle")
    b += text(820, 850, "Higher movability means higher collision energy, so a robot should", 22, 400, INK2)
    b += text(820, 882, "treat those pixels differently. Labels come from a mapping table over", 22, 400, INK2)
    b += text(820, 914, "COCO-Stuff classes, cross-checked by annotators.", 22, 400, INK2)
    b += text(820, 962, "ELEG5491 course project, CUHK, 2025 · tile colours are the model's class overlay", 20, 400, MUTED)
    return wrap(b)

if __name__ == "__main__":
    figs = {"fig-mmsafeaware-two-failures": f1, "fig-chain-of-jailbreak": f2,
            "fig-gui-agent-interface-noise": f3, "fig-skill-firewall": f4,
            "fig-memslot-pipeline": f5, "fig-movability-segmentation": f6}
    os.makedirs("out", exist_ok=True)
    for name, fn in figs.items():
        open(f"out/{name}.svg", "w", encoding="utf-8").write(fn())
        print("wrote", name)
