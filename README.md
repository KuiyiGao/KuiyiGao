### Hi — I'm Cory (Kuiyi) Gao.

I work on **AI agent safety**: I build the benchmarks that show how agents fail once they leave the lab, and the runtime defenses that catch those failures in production.

The question I keep coming back to — **when an agent does something it shouldn't, does anything actually see it?** On stored runs of 65 malicious agent skills, our runtime detector flagged *none* of them. Not because it judged wrongly: 46 of the 65 never produced traffic a monitor could observe. Reported recall was measuring the wrong thing. That study is what I'm writing up now.

Undergraduate at UNC-Chapel Hill · B.A. Computer Science, 2027 · applying for Fall 2027 PhD programs
[Homepage](https://kuiyigao.github.io) · [Google Scholar](https://scholar.google.com/citations?user=Yobg_TQAAAAJ) · [CV](https://kuiyigao.github.io/Kuiyi_Gao_CV.pdf) · kuiyigao@unc.edu

---

### Recently

| | |
|---|---|
| **Sep 2026** | Started at UNC-Chapel Hill as a junior transfer |
| **Aug 2026** | Submitted our GUI-agent robustness benchmark — 42 interface-noise types, 7 agent frameworks (co-first author) |
| **Jul 2026** | Finished the Agent Skill Firewall at MBZUAI UGRIP; writing up the measurement study behind it |
| **Jul 2025** | Two papers at **ACL 2025** — one main conference, one Findings |

### Papers

**Can't See the Forest for the Trees: Benchmarking Multimodal Safety Awareness for Multimodal LLMs** · `ACL 2025 Main` <br/>
[anthology](https://aclanthology.org/2025.acl-long.832/) · [arXiv](https://arxiv.org/abs/2502.11184) <br/>
Multimodal models miss unsafe intent when it is split across image and text — and refuse harmless requests for the same reason. We built the benchmark that separates the two failures.

**Chain-of-Jailbreak Attack for Image Generation Models via Step by Step Editing** · `Findings of ACL 2025` <br/>
[anthology](https://aclanthology.org/2025.findings-acl.571/) · [arXiv](https://arxiv.org/abs/2410.03869) <br/>
Never ask for the unsafe image at once. Every edit step is individually benign, so no single step is the one a filter can refuse. I designed the attack, ran the experiments, and wrote the paper.

**A Dynamic Cross-Platform Benchmark for GUI-Agent Robustness under Real-World Interface Noise** · `under review, 2026` · co-first author <br/>
Noise does not simply lower an agent's success rate — it redirects the trajectory and raises the rate of unsafe actions. Success rate alone hides that.

<!-- ── FIGURE STRIP ────────────────────────────────────────────────────────────
     Put 2–3 figures in assets/ (conventions: assets/README.md), then delete this
     opening marker and the closing one below.

<table>
  <tr>
    <td width="33%"><img src="assets/fig-recall-factorization.png" width="100%" alt=""/><br/>
        <sub><b>Recall factorizes.</b> P(execute)·P(observe|execute)·P(detect|observed) — the middle term is the one that bit us</sub></td>
    <td width="33%"><img src="assets/fig-skill-firewall.png" width="100%" alt=""/><br/>
        <sub><b>Agent Skill Firewall.</b> Intent → action → result, checked through a canary-seeded proxy</sub></td>
    <td width="33%"><img src="assets/fig-noise-trajectories.png" width="100%" alt=""/><br/>
        <sub><b>Interface noise redirects trajectories.</b> Same task, same agent, one overlay</sub></td>
  </tr>
</table>

──────────────────────────────────────────────────────────────────────────── -->

### Things I built

Each repository carries its own `docs/`: the question it answers, the claim, the evidence, and one command that reproduces it.

| | |
|---|---|
| **[OpenClaw-Skill-Hack](https://github.com/KuiyiGao/OpenClaw-Skill-Hack)** | **Agent Skill Firewall** — scans a skill statically, then verifies intent against action against result through a canary-seeded proxy. Every PASS / DEFER / BLOCK keeps the evidence it was made from, so a block can be re-derived instead of taken on faith. |
| **[Distorted-OCR-Compression](https://github.com/KuiyiGao/Distorted-OCR-Compression)** | **MemSlot** — 32 learnable memory slots learn which spans of a contract matter *before* anyone asks a question; the salient spans are compressed through an OCR model. CUAD, ten control arms. |
| **[QuickMotionDetection](https://github.com/KuiyiGao/QuickMotionDetection)** | **Movability segmentation** — COCO-Stuff relabelled into four levels of "can this move?", as a perception prior for embodied safety. mIoU 0.638 @ 58 FPS. |

### How I try to work

- **Report the measurement that complicates the story.** The 0-out-of-65 above is the least flattering number in my own system, and it is the one worth publishing.
- **Every number should be checkable.** If it is here, there is a paper, a repo, or a script behind it — and if it came from a corpus only I have, I say so.
- **Build it before writing about it.** Every paper above started as something that ran.
