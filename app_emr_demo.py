import gradio as gr
import whisper

whisper_model = whisper.load_model("base")

def simple_soap_template(transcript):
    return f"""Subjective:
Draft from transcript. Review required.
Transcript evidence:
{transcript[:1200]}

Objective:
Extract objective findings only if stated in the transcript.

Assessment:
Do not infer final diagnosis. Summarize documented clinical impression only.

Plan:
Include only plans explicitly stated. If absent, write "Not documented".

⚠️ Clinician review required."""

def audio_to_soap(audio_file):
    if audio_file is None:
        return "", "Please upload audio."
    result = whisper_model.transcribe(audio_file, fp16=False)
    transcript = result["text"]
    soap = simple_soap_template(transcript)
    return transcript, soap

with gr.Blocks(title="Whisper EMR Demo") as demo:
    gr.Markdown("# 🏥 Whisper → SOAP Note Demo")
    gr.Markdown("Upload clinical audio to generate a draft SOAP note. **For educational use only.**")

    audio_input = gr.Audio(type="filepath", label="Upload Audio")
    btn = gr.Button("Transcribe & Generate SOAP")

    transcript_out = gr.Textbox(label="Transcript", lines=8)
    soap_out = gr.Textbox(label="SOAP Draft", lines=15)

    btn.click(fn=audio_to_soap, inputs=audio_input, outputs=[transcript_out, soap_out])

if __name__ == "__main__":
    demo.launch()

