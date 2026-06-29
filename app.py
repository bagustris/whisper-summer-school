import gradio as gr
import whisper

model = whisper.load_model("base")

def transcribe_audio(audio_file):
    if audio_file is None:
        return "Please upload or record audio."
    result = model.transcribe(
        audio_file,
        language="en",
        task="transcribe",
        fp16=False
    )
    return result["text"]

demo = gr.Interface(
    fn=transcribe_audio,
    inputs=gr.Audio(type="filepath", label="Upload or record audio"),
    outputs=gr.Textbox(label="Transcript", lines=10),
    title="Whisper Speech-to-Text Demo",
    description="Upload an audio file and transcribe it using OpenAI Whisper."
)

if __name__ == "__main__":
    demo.launch()

