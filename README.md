# Kuiyi (Cory) Gao

Undergraduate researcher in **AI safety and agent robustness** · B.A. Computer Science, UNC-Chapel Hill (expected May 2027; transferred from CUHK)

[Homepage](https://kuiyigao.github.io) · [ACL Anthology](https://aclanthology.org/people/k/kuiyi-gao/) · [CV](https://kuiyigao.github.io/Kuiyi_Gao_CV.pdf) · kuiyigao@unc.edu

---

### What I work on

One line runs through everything below: a **benchmark** locates a failure, an **attack** shows how it is exploited, a **defense** closes it — measured where the system is actually deployed.

- **GUI-agent robustness** under real interface noise (overlays, dynamic content, deceptive widgets): how noise changes trajectories and the rate of unsafe actions, not just success.
- **Agent supply chain**: runtime, evidence-producing defenses for the skills and tools agents load — does the code do what it declared?
- **Multimodal safety**: safety awareness and jailbreak resistance in multimodal and image-generation models.
- *Next*: persona and memory safety — behavioural drift under long interaction, and audits of what an agent retains (proposal stage).

### Publications

1. **Can't See the Forest for the Trees: Benchmarking Multimodal Safety Awareness for Multimodal LLMs** — W. Wang, X. Liu, **K. Gao**, J. Huang, Y. Yuan, P. He, S. Wang, Z. Tu. *ACL 2025 (Main)*. [Anthology](https://aclanthology.org/2025.acl-long.832/) · [arXiv](https://arxiv.org/abs/2502.11184)
2. **Chain-of-Jailbreak Attack for Image Generation Models via Step by Step Editing** — W. Wang, **K. Gao**, Y. Yuan, J. Huang, Q. Liu, S. Wang, W. Jiao, Z. Tu. *Findings of ACL 2025*. [Anthology](https://aclanthology.org/2025.findings-acl.571/) · [arXiv](https://arxiv.org/abs/2410.03869)
3. **RealGUINoise: A Dynamic Cross-Platform Benchmark for GUI Agent Robustness under Real-World Interface Noise** — **K. Gao**\* and collaborators at CUHK (co-first author). *Under review, 2026.* Preprint on request.

### Selected repositories

| Repo | What it is | Status |
|---|---|---|
| [OpenClaw-Skill-Hack](https://github.com/KuiyiGao/OpenClaw-Skill-Hack) | Agent Skill Firewall — runtime intent–action–result verification for agent skills; 23 passing tests, CI | MBZUAI UGRIP 2026 |
| [Distorted-OCR-Compression](https://github.com/KuiyiGao/Distorted-OCR-Compression) | MemSlot saliency + DeepSeek-OCR compression for long contracts (CUAD) | UNC COMP 586 project |
| [QuickMotionDetection](https://github.com/KuiyiGao/QuickMotionDetection) | Movability segmentation (DeepLabV3 + custom ASPP), mIoU 0.638 @ 58 FPS | CUHK ELEG 5491 project |
| cuhk-ai-ta | Course AI teaching assistant that guides instead of answering (Flask, two-stage LLM pipeline) | CUHK GEWS2011, 2025 (repo link after cleanup) |

### Background

- 2026 – 2027 · UNC-Chapel Hill, B.A. Computer Science (exchange Jan – May 2026, then transfer)
- 2026 Jun – Jul · MBZUAI UGRIP 2026, Skill Firewall for AI agents (Dr. Steve Liu's team)
- 2025 Sep – · CUHK, Prof. Michael R. Lyu — GUI-agent robustness benchmark
- 2025 May – Aug · CUHK, Prof. Farzan Farnia — kernel-based novelty scores for text (summer research)
- 2023 Dec – 2025 Feb · Tencent AI Lab (now Hunyuan), with Zhaopeng Tu and Wenxuan Wang — papers [1] and [2]
- 2023 – 2026 · The Chinese University of Hong Kong, B.Sc. program in Computer Science, ELITE Stream

<sub>Applying to PhD programs for Fall 2027 · AI safety · agent security · trustworthy human–AI interaction.</sub>
