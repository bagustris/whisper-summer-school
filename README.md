# 🎙️ Whisper Summer School — Speech AI & Healthcare

Practical project from the Summer School lecture on OpenAI Whisper,
covering ASR fundamentals, local deployment, Gradio web apps, and EMR SOAP note generation.

## 📋 Requirements

- Python 3.9–3.11
- FFmpeg installed
- 8 GB RAM minimum (GPU recommended for large models)

## ⚙️ Installation

```bash
# Clone repo
git clone https://github.com/YOUR_USERNAME/whisper-summer-school.git
cd whisper-summer-school

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

## 🔧 Install FFmpeg

```bash
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt install ffmpeg -y

# Windows
winget install Gyan.FFmpeg
```

## 🚀 Usage

### Command Line Transcription
```bash
whisper audio/sample_english.mp3 --model base --language English
```

### Python Transcription
```bash
python transcribe.py
```

### Gradio Web App
```bash
python app.py
```

### EMR SOAP Demo
```bash
python app_emr_demo.py
```

## 📁 Project Structure

```
whisper-summer-school/
├── audio/               # Input audio files (not tracked by git)
├── outputs/
│   ├── transcripts/     # Generated transcripts
│   └── soap_notes/      # Generated SOAP drafts
├── app.py               # Basic Gradio app
├── app_emr_demo.py      # Full pipeline: audio → SOAP
├── transcribe.py        # Python transcription script
├── soap_from_transcript.py  # Medical LLM SOAP generation
├── requirements.txt
└── README.md
```

## ⚠️ Disclaimer

This project is for **educational purposes only**.
- Do NOT use real patient audio without consent and ethics approval.
- SOAP drafts must be reviewed by a licensed clinician before use.
- Voice data is sensitive personal data — handle responsibly.

## 📚 References

- [OpenAI Whisper](https://github.com/openai/whisper)
- [Gradio Documentation](https://www.gradio.app/docs)
- [FFmpeg](https://ffmpeg.org/)

