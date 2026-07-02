# 🏥 Voice to SOAP — Pipeline Transkripsi Medis

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-6.0+-orange.svg)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-macOS%20%7C%20Linux%20%7C%20Windows-lightgrey.svg)]()

**🇮🇩 Bahasa Indonesia · [🇬🇧 English](README.md)**

</div>

---

Pipeline AI untuk **transkripsi audio medis otomatis** dan pembuatan **catatan SOAP** menggunakan OpenAI Whisper + LLM medis lokal.

> ⚠️ **Disclaimer:** Output AI bersifat *advisory* dan wajib ditinjau oleh tenaga medis profesional sebelum digunakan secara klinis.

## ✨ Fitur Utama

- 🎙️ **Transkripsi otomatis** percakapan dokter-pasien via OpenAI Whisper
- 📋 **Generasi SOAP note** terstruktur (Subjective / Objective / Assessment / Plan)
- 🔒 **PII De-identification** — nama & data sensitif otomatis di-mask (via OpenMed)
- 🍎 **Apple Silicon optimized** — auto-detect MPS/MLX
- ⚡ **Multi-backend LLM** — OpenMed, Ollama, atau HuggingFace
- 🖥️ **Gradio UI** — antarmuka web dengan mikrofon, SOAP viewer & download

---

## 🗂️ Struktur Project

```
voice-to-soap/
├── main.py                  # Pipeline utama (CLI)
├── config.py                # Konfigurasi terpusat (device, model, backend)
├── transcribe.py            # Modul transkripsi Whisper
├── soap_generator.py        # SOAP via Ollama (medllama2, mistral, dll)
├── soap_openmed.py          # SOAP via OpenMed (NER + PII de-id)
├── app.py                   # Gradio UI — transkripsi sederhana
├── app_emr_demo.py          # Gradio UI — demo EMR lengkap
├── requirements.txt         # Dependensi Python
├── legacy/
│   └── soap_from_transcript.py  # HuggingFace backend (arsip)
├── audio/                   # File audio input (tidak di-commit)
└── outputs/                 # Hasil transkrip & SOAP (tidak di-commit)
```

---

## ⚙️ Instalasi

### 1. Clone & buat virtual environment

```bash
git clone https://github.com/<username>/voice-to-soap.git
cd voice-to-soap

python3 -m venv .venv
source .venv/bin/activate        # macOS / Linux
# .venv\Scripts\activate         # Windows
```

### 2. Install dependensi

```bash
pip install -r requirements.txt
```

### 3. Install backend LLM (pilih salah satu)

#### 🥇 OpenMed — Direkomendasikan

```bash
pip install "openmed[mlx]"   # Apple Silicon (M1/M2/M3/M4)
pip install openmed           # CPU atau NVIDIA
```

#### 🦙 Ollama — Lokal, mudah digunakan

```bash
# Install Ollama: https://ollama.com
ollama pull medllama2       # Model medis (3.8 GB)
ollama pull mistral         # General purpose (4 GB)
ollama pull llama3.2        # Ringan & cepat (2 GB)

ollama serve                # Jalankan server (terminal terpisah)
```

---

## 🚀 Cara Penggunaan

### CLI

```bash
python main.py audio/sample.mp3                              # Default (OpenMed)
python main.py audio/sample.mp3 --backend ollama --model medllama2
python main.py audio/sample.mp3 --no-soap                   # Transkripsi saja
python main.py audio/sample.mp3 --whisper-model small --lang en
```

### Semua Flag CLI

| Flag | Shorthand | Default | Keterangan |
|------|-----------|---------|------------|
| `--backend` | `-b` | `openmed` | `openmed` / `ollama` / `hf` |
| `--model` | `-m` | `medllama2` | Nama model Ollama |
| `--whisper-model` | `-w` | `base` | Ukuran model Whisper |
| `--lang` | `-l` | `id` | `id` / `en` / `auto` |
| `--no-soap` | — | `False` | Skip generasi SOAP |

### Gradio Web UI

```bash
python app_emr_demo.py
```

> 🎙️ **Mikrofon:** Selalu buka via **`http://localhost:PORT`** — bukan `http://0.0.0.0:PORT`
> Browser hanya mengizinkan akses mikrofon di [secure context](https://developer.mozilla.org/en-US/docs/Web/Security/Secure_Contexts),
> dan `localhost` dianggap secure meskipun tanpa HTTPS.

#### Fitur Web UI

| Fitur | Keterangan |
|-------|-----------|
| 🎙️ Upload / Rekam | Upload file audio atau rekam via mikrofon |
| 🤖 Pilih Backend | `openmed` / `ollama` / `hf` |
| 🦙 Pilih Model Ollama | Dropdown dinamis dari `ollama list` |
| 🎙️ Pilih Whisper Model | `tiny` → `large-v3-turbo` |
| 🌐 Pilih Bahasa | `id` / `en` / `auto` |
| 🔒 De-identifikasi PII | Mask nama & data sensitif |
| 📝 Transkrip Viewer | Tampil di tab Transkrip |
| 📋 SOAP Viewer | Tampil di tab SOAP Note |
| 🗂️ JSON Viewer | Tampil di tab JSON |
| ⬇️ Download | `transcript.txt` · `soap.txt` · `soap.json` |

---

## 📦 Dataset

Project ini menggunakan dataset **[Audio Recording Whisper](https://www.kaggle.com/datasets/najamahmed97/audio-recording-whisper)** oleh najamahmed97 (Kaggle) sebagai data benchmark.

**Isi:** Rekaman audio percakapan dokter-pasien dalam bahasa Inggris, dilengkapi **transkrip ground-truth** — ideal untuk menguji pipeline dan mengukur akurasi transkripsi (Word Error Rate).

### Download dataset

**Opsi A — Manual (tanpa akun Kaggle):**

1. Buka [halaman dataset](https://www.kaggle.com/datasets/najamahmed97/audio-recording-whisper) di browser
2. Klik tombol **Download** → simpan file ZIP
3. Ekstrak ke folder `audio/`:

```bash
unzip audio-recording-whisper.zip -d audio/
```

**Opsi B — Kaggle CLI:**

```bash
pip install kaggle
# Letakkan kaggle.json di ~/.kaggle/, lalu:
kaggle datasets download -d najamahmed97/audio-recording-whisper -p audio/ --unzip
```

### Jalankan pipeline pada dataset

```bash
# Satu file
python main.py audio/<file>.wav --whisper-model base --language en

# Batch — semua file WAV (bash)
for f in audio/*.wav; do
    python main.py "$f" --language en --whisper-model small
done
```

### Evaluasi akurasi transkripsi (WER)

Karena dataset menyertakan transkrip referensi, akurasi Whisper dapat diukur dengan Word Error Rate:

```bash
pip install jiwer

python - <<'EOF'
from jiwer import wer
from pathlib import Path

for ref_path in Path("audio").glob("*.txt"):
    hyp_path = Path("outputs") / f"transcript_{ref_path.stem}.txt"
    if hyp_path.exists():
        ref = ref_path.read_text().strip()
        hyp = hyp_path.read_text().strip()
        print(f"{ref_path.stem}: WER = {wer(ref, hyp):.1%}")
EOF
```

---

## 🤖 Perbandingan Backend LLM

| Backend | Keunggulan | Kelemahan | Kebutuhan |
|---------|-----------|-----------|-----------|
| **OpenMed** | PII de-id, 1000+ model medis, MLX native | Perlu install extra | `pip install "openmed[mlx]"` |
| **Ollama** | Mudah, model bisa diganti, stabil | Perlu `ollama serve` | `ollama pull medllama2` |
| **HuggingFace** | Tanpa server tambahan | Butuh VRAM besar (14GB+) | GPU recommended |

---

## 🎙️ Model Whisper

| Model | VRAM | Kecepatan | Akurasi | Rekomendasi |
|-------|------|-----------|---------|-------------|
| `tiny` | ~1 GB | ⚡⚡⚡⚡ | ⭐⭐ | Testing cepat |
| `base` | ~1 GB | ⚡⚡⚡ | ⭐⭐⭐ | **Default** |
| `small` | ~2 GB | ⚡⚡ | ⭐⭐⭐⭐ | Recommended |
| `medium` | ~5 GB | ⚡ | ⭐⭐⭐⭐⭐ | Akurasi tinggi |
| `large-v3-turbo` | ~6 GB | ⚡⚡ | ⭐⭐⭐⭐⭐ | Best quality |

---

## 📋 Format Output SOAP

```
=======================================================
         CATATAN MEDIS — FORMAT SOAP
  Dibuat : 2026-06-30T01:25:00
  Model  : medllama2:latest
=======================================================

[S — Subjective (Keluhan Pasien)]
• Dizziness selama beberapa bulan
• Hearing loss dan tinnitus (ringing in ears)

[O — Objective (Temuan Klinis)]
• Pasien tampak comfortable
• Blood pressure 120/80, HR 72

[A — Assessment (Penilaian)]
• Consistent with Meniere's disease

[P — Plan (Rencana Tindakan)]
• Prescribe betahistine 16mg twice daily
• Referral to audiology
• Follow-up in 4 weeks
=======================================================
```

Output disimpan otomatis ke `outputs/`:
- `transcript_<nama>_<timestamp>.txt`
- `soap_<nama>_<timestamp>.txt`
- `soap_<nama>_<timestamp>.json`

---

## 🛠️ Konfigurasi (`config.py`)

```python
BACKEND = "ollama"               # "openmed" | "ollama" | "hf"

whisper_cfg.model_size = "base"  # tiny | base | small | medium | large-v3-turbo
whisper_cfg.language   = "auto"  # "id" | "en" | "auto"

ollama_cfg.model = "llama3.2"

openmed_cfg.deidentify_before_soap = True
```

---

## 🔒 Privasi & Keamanan

- ✅ **100% lokal** — tidak ada data dikirim ke server eksternal
- ✅ **PII De-identification** — nama pasien & data sensitif otomatis di-mask
- ✅ **HIPAA-aware** — OpenMed mendukung 247 checkpoint de-identifikasi
- ❌ **Jangan commit** data pasien ke repository publik

---

## 🐛 Troubleshooting

| Masalah | Solusi |
|---------|--------|
| `FP16 not supported on CPU` | Sudah di-suppress otomatis |
| Mikrofon tidak aktif | Buka via `http://localhost:PORT`, bukan `http://0.0.0.0:PORT` |
| `ollama: model not found` | Jalankan `ollama pull medllama2` |
| NumPy / Numba conflict | `pip install "numpy==1.26.4"` |
| MPS out of memory | Gunakan `--whisper-model tiny` |

---

## 🗺️ Roadmap

- [x] Transkripsi Whisper multi-device (CPU / MPS / CUDA)
- [x] SOAP generation via Ollama
- [x] SOAP generation via OpenMed (NER + PII de-id)
- [x] Auto-detect Apple Silicon / NVIDIA / CPU
- [x] Multi-layer response parser (JSON → header → regex → fallback)
- [x] Gradio UI — transkripsi sederhana (`app.py`)
- [x] Gradio UI — EMR demo lengkap (`app_emr_demo.py`)
- [x] SOAP viewer & download (txt + json) di Web UI
- [x] Mikrofon aktif di localhost (secure context fix)
- [ ] Whisper `large-v3-turbo` benchmark di Apple Silicon
- [ ] Output PDF dari SOAP note
- [x] Batch processing multiple audio files (lihat bagian Dataset)

---

## 👥 Kontribusi

Pull request dan issue sangat disambut! Pastikan:
1. Tidak menyertakan data pasien nyata
2. Test pipeline: `python main.py audio/sample.mp3 --no-soap`
3. Update README jika menambah fitur baru

---

## 📄 Lisensi

MIT License — bebas digunakan untuk keperluan edukasi dan riset.