import whisper
from pathlib import Path

model = whisper.load_model("base")
audio_path = "audio/sample_english.mp3"

result = model.transcribe(
    audio_path,
    language="en",
    task="transcribe"
)

transcript = result["text"]

Path("outputs/transcripts").mkdir(parents=True, exist_ok=True)
Path("outputs/transcripts/sample_english.txt").write_text(transcript, encoding="utf-8")

print("Transcription complete:")
print(transcript)

