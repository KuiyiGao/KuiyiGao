### Hi — I'm Cory (Kuiyi) Gao.

I work on **trustworthy AI** — how systems behave once they leave the lab and meet real interfaces, real tools and real people. So far that has meant multimodal safety benchmarks, jailbreak attacks and the defenses against them, agent robustness under interface noise, and runtime evidence for what an agent actually did.

Undergraduate at UNC-Chapel Hill · B.A. Computer Science, 2027 · applying for Fall 2027 PhD programs<br/>
[Homepage](https://kuiyigao.github.io) · [Google Scholar](https://scholar.google.com/citations?user=Yobg_TQAAAAJ) · [CV](https://kuiyigao.github.io/Kuiyi_Gao_CV.pdf) · kuiyigao@unc.edu

---

### Papers

<table>
<tr>
<td width="36%" valign="top"><a href="assets/fig-mmsafeaware-two-failures.png"><img src="assets/fig-mmsafeaware-two-failures.png" width="100%" alt="Safety awareness has two failure modes: missing unsafe intent that is split across image and text, and over-refusing benign input. GPT-4V calls 36.1% of unsafe inputs safe and 59.9% of benign inputs unsafe."/></a></td>
<td width="64%" valign="top"><b>Can't See the Forest for the Trees: Benchmarking Multimodal Safety Awareness for Multimodal LLMs</b> · <code>ACL 2025 Main</code><br/>
<a href="https://aclanthology.org/2025.acl-long.832/">anthology</a> · <a href="https://arxiv.org/abs/2502.11184">arXiv</a> · <a href="https://github.com/Jarviswang94/MMSafetyAwareness">code &amp; data</a><br/><br/>
Multimodal models miss unsafe intent when it is split across the image and the text, and refuse harmless requests for the same reason. The benchmark scores both failures separately; we then fine-tuned against it. Third author.</td>
</tr>
<tr>
<td valign="top"><a href="assets/fig-chain-of-jailbreak.png"><img src="assets/fig-chain-of-jailbreak.png" width="100%" alt="One harmful request split into a chain of individually harmless edits. Bypasses safeguards in over 60% of cases versus 14% for prior methods; Think Twice Prompting defends over 95%."/></a></td>
<td valign="top"><b>Chain-of-Jailbreak Attack for Image Generation Models via Step by Step Editing</b> · <code>Findings of ACL 2025</code><br/>
<a href="https://aclanthology.org/2025.findings-acl.571/">anthology</a> · <a href="https://arxiv.org/abs/2410.03869">arXiv</a> · <a href="https://github.com/Jarviswang94/Chain-of-Jailbreak">code &amp; data</a><br/><br/>
The attack decomposes one harmful request into a chain of individually benign edits, so no single step is one a filter would refuse and the filter never sees the composition. Second author; I designed the attack methodology, ran most of the attack and defense experiments, and wrote the paper and the rebuttal.</td>
</tr>
<tr>
<td valign="top"><a href="assets/fig-gui-agent-interface-noise.png"><img src="assets/fig-gui-agent-interface-noise.png" width="100%" alt="The same task on a clean interface and on a noisy one with an overlay, shifted content and a look-alike control: the agent takes a different action, sometimes an unsafe one."/></a></td>
<td valign="top"><b>GUI-agent robustness under interface noise</b> · <code>under review, 2026</code> · co-first author<br/><br/>
Real interfaces are noisy: overlays, dynamic content, deceptive widgets. Interface noise does not only lower success rate; it also changes which action an agent takes and raises the rate of unsafe actions.</td>
</tr>
</table>

### Things I built

<table>
<tr>
<td width="36%" valign="top"><a href="assets/fig-skill-firewall.png"><img src="assets/fig-skill-firewall.png" width="100%" alt="Agent Skill Firewall pipeline: skill bundle, static pre-scan, canary-seeded proxy, intent versus action versus result, PASS / DEFER / BLOCK. On stored runs of 65 malicious skills, 46 produced no proxy-visible egress and 0 were flagged."/></a></td>
<td width="64%" valign="top"><b><a href="https://github.com/KuiyiGao/OpenClaw-Skill-Hack">OpenClaw-Skill-Hack</a> — Agent Skill Firewall</b><br/><br/>
A runtime egress firewall for agent skills. It scans a skill statically, then verifies intent against action against result through a canary-seeded proxy; each PASS / DEFER / BLOCK is recorded with the evidence it was derived from. Built with a four-student team at MBZUAI UGRIP 2026; I built the runtime firewall.<br/><br/>
Then I measured whether the check is reached at all: on stored runs of 65 malicious skills the detector flagged 0/65 — 46 of them produced no proxy-visible traffic, so the detector was never reached. Manuscript in preparation.</td>
</tr>
<tr>
<td valign="top"><a href="assets/fig-memslot-pipeline.png"><img src="assets/fig-memslot-pipeline.png" width="100%" alt="MemSlot pipeline: contract text, frozen RoBERTa with 32 memory slots, saliency-distorted rendering, DeepSeek-OCR vision encoder, QA reader scored with CUAD metrics; next to a rendered page where larger, redder words are more important."/></a></td>
<td valign="top"><b><a href="https://github.com/KuiyiGao/Distorted-OCR-Compression">Distorted-OCR-Compression</a> — MemSlot</b><br/><br/>
32 learnable memory slots on a frozen encoder learn which spans of a contract matter <i>before</i> anyone asks a question; those spans are rendered larger and compressed through an OCR model. Saliency is trained on train-split text only, so nothing about the questions leaks in. Evaluated on CUAD against ten control arms.</td>
</tr>
<tr>
<td valign="top"><a href="assets/fig-movability-segmentation.jpg"><img src="assets/fig-movability-segmentation.jpg" width="100%" alt="Movability segmentation: four prediction tiles after 50 epochs beside the four movability levels; best mIoU 0.638 at 58 FPS."/></a></td>
<td valign="top"><b><a href="https://github.com/KuiyiGao/QuickMotionDetection">QuickMotionDetection</a> — Movability segmentation</b><br/><br/>
COCO-Stuff relabelled into four levels of "can this move?", with DeepLabV3 and a custom ASPP head — a perception prior for embodied safety. mIoU 0.638 at 58 FPS. Course project at CUHK.</td>
</tr>
</table>
