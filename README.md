# NeuroCreative Platform

> Unified backend and frontend for EEG-driven creativity using Muse 2 and WHOOP.

---

## Overview

The **NeuroCreative Platform** is the central integration layer for Edward's neurofeedback and biometric creative stack. It connects **Muse 2 EEG brainwave data** with **WHOOP 4.0 recovery metrics** to power adaptive creative workflows, neurodivergent execution tools, and real-time brain-state visualization.

This is the primary MVP repository — all experimental React/ML work has been moved to `_archive/` to keep this codebase focused and stable.

---

## Status

| Item | Status |
|------|--------|
| Active Development | ✅ Yes |
| Backend (Python) | ✅ Functional |
| Frontend (Viewer) | ✅ Simple HTML/JS |
| EEG Streaming | ✅ Python WebSocket |
| Muse 2 Support | ✅ Via Mind Monitor |
| WHOOP Integration | 🔄 In Progress |
| React + ML Frontend | 🗃 Archived (`_archive/`) |

---

## Architecture

```
neurocreative-platform/
├── backend/          # Python WebSocket server, EEG data processing
├── frontend/         # Simple HTML/JS viewer for live data
├── _archive/         # Legacy React + Three.js + TensorFlow (reference only)
├── requirements.txt  # Python dependencies
├── .gitignore
└── README.md
```

---

## Features

- Real-time EEG data streaming via Python WebSocket
- Muse 2 headband integration via Mind Monitor (OSC)
- Live brainwave band display (alpha, beta, theta, delta, gamma)
- WHOOP 4.0 HRV + recovery data overlay (planned)
- Neurodivergent execution state mapping
- Stable `v0.1-mvp` baseline for iterative builds

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| EEG Hardware | Muse 2 Headband |
| Biometric Wearable | WHOOP 4.0 |
| Data Bridge | Mind Monitor (OSC) |
| Backend | Python 3.9+, asyncio, WebSocket |
| Frontend | HTML/CSS/JS (minimal viewer) |
| Archived Frontend | React + Three.js (see `_archive/`) |
| Archived ML | TensorFlow (see `_archive/`) |

---

## Getting Started

### Prerequisites

- Python 3.9+
- Muse 2 headband + Mind Monitor app
- Mind Monitor configured for OSC output to local machine

### Installation

```bash
git clone https://github.com/edwardemoryphotography/neurocreative-platform.git
cd neurocreative-platform
pip install -r requirements.txt
```

### Run

```bash
cd backend
python main.py
```

Open `frontend/index.html` in a browser to view the live EEG stream.

---

## Versioning

| Tag | Description |
|-----|-------------|
| `v0.1-mvp` | Stable baseline — Python backend + simple frontend |
| `main` | Active development branch |

---

## Roadmap

- [ ] WHOOP API integration (HRV + strain + recovery scores)
- [ ] EEG + HRV correlation dashboard
- [ ] Session state export (JSON/CSV)
- [ ] Neurofeedback audio cue system
- [ ] Adaptive UI based on brain state (focus vs. rest)
- [ ] Cross-repo integration with `muse-neurofeedback`

---

## Related Repos

- [`muse-neurofeedback`](https://github.com/edwardemoryphotography/muse-neurofeedback) — Standalone neurofeedback application
- [`legacy-codex`](https://github.com/edwardemoryphotography/legacy-codex) — Neurodivergent execution frameworks

---

## Audit Notes

- **Last reviewed**: 2025 — Identified as stale-active during GitHub audit
- **Action taken**: README fully documented; React + ML moved to `_archive/`
- **MVP Tag**: `v0.1-mvp` stable checkpoint preserved
- **Priority**: High — primary integration hub for EEG + biometric stack

---

*Part of the edwardemoryphotography GitHub ecosystem.*
