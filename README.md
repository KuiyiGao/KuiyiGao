# Kuiyi (Cory) Gao

I am an undergraduate at UNC-Chapel Hill, graduating in May 2027. I work on AI safety, especially agent evaluation, multimodal safety, and runtime controls. My research has included work with Tencent AI Lab, CUHK, and MBZUAI UGRIP. I am applying to PhD programs for Fall 2027.

[Homepage](https://kuiyigao.github.io), [CV](https://kuiyigao.github.io/Kuiyi_Gao_CV.pdf), [Google Scholar](https://scholar.google.com/citations?user=Yobg_TQAAAAJ), and [Email](mailto:kuiyigao@unc.edu)

## Research

### RealGUINoise

**Co-first author. Under review.** RealGUINoise evaluates GUI agents on paired web and Android tasks before and after realistic interface changes. I built benchmark tasks, designed the evaluation protocol, implemented automated judging, and ran paired experiments.

### RuntimeTickets

**First author. Under review at ICLR 2027.** RuntimeTickets uses task-specific contracts to narrow the permissions available to third-party agent skills and records the requests and effects behind each decision. I designed the method, built the runtime firewall with the UGRIP team, and lead experiments and writing. [System code](https://github.com/KuiyiGao/OpenClaw-Skill-Hack)

### MMSafeAware

**Third author. ACL 2025.** The benchmark separates missed unsafe content from false alarms on benign image and text pairs. I worked on benchmark construction, evaluation, vision-centric fine-tuning, submission, and rebuttal. [Paper](https://aclanthology.org/2025.acl-long.832/) and [Code](https://github.com/Jarviswang94/MMSafetyAwareness)

### Chain-of-Jailbreak

**Second author. Findings of ACL 2025.** This study tests safety failures that emerge across multi-turn image editing. I designed the method and defense, contributed benchmark data, ran most experiments, and prepared figures, writing, and rebuttal. [Paper](https://aclanthology.org/2025.findings-acl.571/) and [Code](https://github.com/Jarviswang94/Chain-of-Jailbreak)

## Projects

### [MemSlot](https://github.com/KuiyiGao/Distorted-OCR-Compression)

MemSlot asks whether a compact set of words can preserve the information needed for document question answering. I trained attention slots over frozen RoBERTa representations to score words and guide page selection before OCR and question answering.

### [Poetry and image variation](https://kuiyigao.github.io/projects.html#poetry)

This project asks how poem style changes the variety of images generated from the same text. I generated image sets with FLUX and Stable Diffusion, then compared saved CLIP-based variation scores across Imagist and Romantic excerpts.

### [Text-KEN](https://kuiyigao.github.io/projects.html#text-ken)

Text-KEN explores whether distributional differences between two text collections can be summarized from sentence embeddings. I implemented RBF-kernel comparisons and spectral-entropy analysis, then tested centering and whitening as embedding preprocessing choices.

### [Movability segmentation](https://github.com/KuiyiGao/QuickMotionDetection)

Movability segmentation treats semantic classes as a practical proxy for whether objects are fixed, movable, human, or vehicle-like. I adapted DeepLabV3 with a custom ASPP head and regrouped COCO-Stuff labels into four movability classes.

## Technical background

**Machine learning and vision:** PyTorch, Hugging Face Transformers, attention models, fine-tuning, semantic segmentation, DeepLabV3, ASPP, and COCO-Stuff label processing.

**Text and statistical methods:** RoBERTa representations, sentence embeddings, RBF kernels, eigendecomposition, spectral entropy, NumPy, SciPy, pandas, and Matplotlib.

**Evaluation and software:** benchmark construction, task design, automated judging, paired experiments, Python, Git, Linux, Docker, browser automation, document rendering, model APIs, and reproducible experiment records.

**Course foundations:** algorithms, machine learning, natural language processing, deep learning, C and Unix systems, and object-oriented design.
