### Hi — I'm Cory (Kuiyi) Gao.

I work on **trustworthy AI** — how systems behave once they leave the lab and meet real interfaces, real tools and real people. Mostly: safety benchmarks, jailbreak attacks and defenses, agent robustness under interface noise, and runtime evidence for what an agent actually did.

<img src="assets/fig-recall-factorization.png" width="100%" alt="Reported recall factorizes into P(execute), P(observe given execute) and P(detect given observed); of 65 malicious skills, 46 produced no observable egress and 0 were flagged"/>

<sub>On stored runs of 65 malicious agent skills, 46 produced no proxy-visible traffic, so the detector was never reached.</sub>

Undergraduate at UNC-Chapel Hill · B.A. Computer Science, 2027 · applying for Fall 2027 PhD programs
[Homepage](https://kuiyigao.github.io) · [Google Scholar](https://scholar.google.com/citations?user=Yobg_TQAAAAJ) · [CV](https://kuiyigao.github.io/Kuiyi_Gao_CV.pdf) · kuiyigao@unc.edu

---

### Papers

**Can't See the Forest for the Trees: Benchmarking Multimodal Safety Awareness for Multimodal LLMs** · `ACL 2025 Main` <br/>
[anthology](https://aclanthology.org/2025.acl-long.832/) · [arXiv](https://arxiv.org/abs/2502.11184) <br/>
Multimodal models miss unsafe intent when it is split across image and text, and refuse harmless requests for the same reason. The benchmark scores both failures separately.

**Chain-of-Jailbreak Attack for Image Generation Models via Step by Step Editing** · `Findings of ACL 2025` <br/>
[anthology](https://aclanthology.org/2025.findings-acl.571/) · [arXiv](https://arxiv.org/abs/2410.03869) <br/>
The attack decomposes one harmful request into a chain of individually benign edits, so no single step is one a filter would refuse. I designed the attack methodology, ran the experiments, and wrote the paper.

**GUI-agent robustness under interface noise** · `under review, 2026` · co-first author <br/>
Interface noise does not only lower success rate; it also changes which action an agent takes and raises the rate of unsafe actions.

### Things I built

<table>
<tr>
<td width="42%"><img src="assets/fig-skill-firewall.png" width="100%" alt="Agent Skill Firewall pipeline: skill bundle, static pre-scan, canary-seeded proxy, intent vs action vs result, PASS DEFER BLOCK"/></td>
<td width="58%"><b><a href="https://github.com/KuiyiGao/OpenClaw-Skill-Hack">OpenClaw-Skill-Hack</a> — Agent Skill Firewall</b><br/>
Scans a skill statically, then verifies intent against action against result through a canary-seeded proxy. Each PASS / DEFER / BLOCK is recorded with the evidence it was derived from.</td>
</tr>
</table>

| | |
|---|---|
| **[Distorted-OCR-Compression](https://github.com/KuiyiGao/Distorted-OCR-Compression)** | **MemSlot** — 32 learnable memory slots learn which spans of a contract matter *before* anyone asks a question; those spans are then compressed through an OCR model. |
| **[QuickMotionDetection](https://github.com/KuiyiGao/QuickMotionDetection)** | **Movability segmentation** — COCO-Stuff relabelled into four levels of "can this move?", as a perception prior for embodied safety. mIoU 0.638 @ 58 FPS. |
