<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff7a18,50:af00ff,100:2e9ef7&height=120&section=header" width="100%" />
</p>

<p align="center">
  <img src="./assets/hero.svg" width="100%" alt="Tejas Gowda S — Junior AI Engineer" />
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=20&duration=2800&pause=900&color=2E9EF7&center=true&vCenter=true&width=620&lines=Junior+AI+Engineer+%40+Kenpath;Training+LLMs+from+scratch+in+Rust+%E2%80%94+FLAME+%F0%9F%94%A5;Building+Sanctum+%E2%80%94+serverless%2C+Tor-routed+chat;Rust+%C2%B7+C%2B%2B+%C2%B7+Python+%C2%B7+Flutter;Guardrails%2C+RAG+%26+agentic+systems" alt="Typing SVG" /></a>
</p>

<p align="center">
  <a href="https://kenpath.io"><img src="https://img.shields.io/badge/Kenpath-Junior_AI_Engineer-ff7a18?style=for-the-badge&labelColor=0b0f1a" /></a>
  <a href="mailto:tejas12gowda@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white&labelColor=0b0f1a" /></a>
  <a href="https://linkedin.com/in/tejas-gowda-sridhara"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=0b0f1a" /></a>
  <a href="https://twitter.com/tejas_gowda_001"><img src="https://img.shields.io/badge/X-000000?style=for-the-badge&logo=x&logoColor=white&labelColor=0b0f1a" /></a>
</p>

---

## ⚡ `cat about.md`

```rust
struct Tejas {
    role:      "Junior AI Engineer @ Kenpath — full stack + AI",
    building:  ["FLAME — LLMs from scratch in Rust", "Sanctum — private P2P messenger"],
    education: "B.E. AI & Data Science, Global Academy of Technology — 2026, 9.5 CGPA 🎓",
    obsessed:  ["LLM internals", "low-level systems", "privacy & security"],
    stack:     ["Rust", "C++", "Python", "Flutter"],
    based_in:  "Bangalore, India 🇮🇳",
    off_hours: ["🎮 games", "🎵 music", "🎬 anime"],
}
```

---

## 🔥 Flagship Work

<table>
<tr>
<td width="50%" valign="top">

### 🔥 FLAME &nbsp;<sub>`RTensorLabs`</sub>
**Framework for Lightweight AI Model Engineering.**

A small, readable **Rust + Candle** framework for training language models **from scratch on one laptop**. Covers the whole pipeline: a BPE tokenizer, a Transformer (RoPE, SwiGLU, RMSNorm), hand-written AdamW and a training run you can pause and resume to the exact same weights. Its logits match a PyTorch reference to within **5e-7**.

- 🧪 **FLAME-Research**: dynamically routed modular models compared against dense and MoE baselines
- 🦀 **Lintless**: the FLAME Rust base model fine-tuned to explain and fix `rustc` errors. A fix only counts if the file compiles afterwards

<a href="https://huggingface.co/spaces/Tejascodex001/flame-visualizer"><img src="https://img.shields.io/badge/🤗_Try_the_Visualizer-FFD21E?style=flat-square&labelColor=0b0f1a" /></a> <a href="https://learn-rust-flame-site.vercel.app"><img src="https://img.shields.io/badge/📘_Learn_FLAME-2e9ef7?style=flat-square&labelColor=0b0f1a" /></a><br/>
<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" /> <img src="https://img.shields.io/badge/Candle-ff7a18?style=flat-square" /> <img src="https://img.shields.io/badge/CUDA-76B900?style=flat-square&logo=nvidia&logoColor=white" /> <img src="https://img.shields.io/badge/LLM_from_scratch-af00ff?style=flat-square" />

</td>
<td width="50%" valign="top">

### 🔒 [Sanctum](https://github.com/Tejascodex001/sanctum) &nbsp;<sub>`beta`</sub>
**Private chat for close friends. No servers, no accounts, no tracking.**

Peer-to-peer Android messenger over **Tor onion services** with **MLS end-to-end encryption**, groups of 50, voice/video calls, offline Wi-Fi/Bluetooth mesh, decoy PIN & panic wipe — and a unique **sigil** per chat to verify nobody's listening.

<img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" /> <img src="https://img.shields.io/badge/Flutter-02569B?style=flat-square&logo=flutter&logoColor=white" /> <img src="https://img.shields.io/badge/Tor-7E4798?style=flat-square&logo=torproject&logoColor=white" /> <img src="https://img.shields.io/badge/MLS-E2EE-2e9ef7?style=flat-square" />

</td>
</tr>
</table>

## 🛠 More Projects

| Project | What it is | Stack |
|---|---|---|
| 🦀 **Lintless** <sub>(RTensorLabs)</sub> | Fine-tuned FLAME model that explains & fixes Rust compiler errors, data mined by mutating real code | Rust · Candle |
| 🛡 **[GuardLayer](https://github.com/Tejascodex001/GuardLayer)** | Defense-in-depth guardrails middleware for LLMs — prompt-injection, jailbreak, toxicity & PII guards with explainable risk scores | Python · MiniLM · NLP |
| 🧱 **[SmartGuard](https://github.com/Tejascodex001/smartguard)** | LLM input/output firewall — DeBERTa classifier (99.7% recall), red-team suite, ~40ms CPU P95 | Python · DeBERTa · ONNX |
| 🎥 **[C++ Vision Engine](https://github.com/Tejascodex001/Cpp-image-and-video-processing-pipeline)** | Zero-allocation real-time image/video pipeline with hand-written convolutions & live telemetry HUD | C++17 · OpenCV · CMake |
| 📈 **[System Anomaly Detector](https://github.com/Tejascodex001/System-anomaly-detector)** | Multithreaded `/proc` telemetry collector with rolling z-score anomaly scoring | Modern C++ · Concurrency |
| 🧬 **[Auto-Immunity for Systems](https://github.com/Tejascodex001/Auto-immunity-for-systems)** | Self-learning cyber-defense: RAG-powered LLM + RL agents in a Dockerized battleground | Python · RL · RAG · Docker |
| 🚚 **[Zip Route](https://github.com/Tejascodex001/delivery-route-app)** | Multi-stop delivery route optimization | Python |

<details>
<summary><b>🗄 Archive</b></summary>

- **[FaceNet](https://github.com/Tejascodex001/FaceNet)** — one-shot face verification with embeddings
- **[Sign Language Translator](https://github.com/Tejascodex001/sign-language)** — real-time ASL → text (79.3% acc.)
- **[Face Recognition Attendance](https://github.com/Tejascodex001/face_recognize_attendance_system)** — automated attendance with OpenCV
</details>

---

## 💼 Experience

```diff
+ Junior AI Engineer · Kenpath                                Sep 2026 — present
!   Full-stack development & AI engineering — kenpath.io

- Trainee Software Engineer Intern · CGI                                    2025
    OCR pipeline with PaddleOCR → structured extraction → RAG document Q&A
```

---

## 🧰 Toolbox

<p align="center">
  <img src="https://skillicons.dev/icons?i=rust,cpp,python,dart,flutter,pytorch,tensorflow,sklearn,opencv&perline=9" /><br/><br/>
  <img src="https://skillicons.dev/icons?i=linux,arch,docker,git,cmake,bash,neovim,vscode,postgres&perline=9" />
</p>

---

## 📊 Stats

<p align="center">
  <img height="165" src="https://github-readme-stats.vercel.app/api?username=Tejascodex001&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0b0f1a&count_private=true" />
  <img height="165" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Tejascodex001&layout=compact&theme=tokyonight&hide_border=true&bg_color=0b0f1a" />
</p>
<p align="center">
  <img src="https://github-readme-activity-graph.vercel.app/graph?username=Tejascodex001&theme=tokyo-night&hide_border=true&bg_color=0b0f1a&area=true" width="95%" />
</p>

---

<p align="center">
  <b>Open to collabs on LLMs, systems programming, privacy tech & security.</b><br/>
  <sub>🏅 Cisco Intro to Cybersecurity · NPTEL Python & Data Science for Engineers · Infosys Python / Front-End / Networking</sub>
</p>

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=Tejascodex001&label=views&color=ff7a18&style=flat-square" />
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2e9ef7,50:af00ff,100:ff7a18&height=100&section=footer" width="100%" />
</p>
