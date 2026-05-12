import gradio as gr

def process_audio(audio):

    with open("outputs/transcript1.txt") as f:
        transcript_1 = f.read()

    with open("outputs/transcript2.txt") as f:
        transcript_2 = f.read()

    primary_user = "Speaker 1"

    response = "Bedroom lights turned on."

    scores = {
        "Speaker 1": 0.91,
        "Speaker 2": 0.42
    }

    return (
        transcript_1,
        transcript_2,
        primary_user,
        response,
        scores
    )

with gr.Blocks() as demo:

    gr.Markdown("# Multi-User Smart Assistant")

    gr.Markdown("## Upload Mixed Audio")

    audio_input = gr.Audio(
        type="filepath",
        label="Mixed Audio Input"
    )

    btn = gr.Button("Process Audio")

    gr.Markdown("## Transcriptions")

    with gr.Row():

        speaker1 = gr.Textbox(
            label="Speaker 1 Transcript"
        )

        speaker2 = gr.Textbox(
            label="Speaker 2 Transcript"
        )

    gr.Markdown("## Primary User Detection")

    primary = gr.Textbox(
        label="Primary User"
    )

    pud_scores = gr.JSON(
        label="PUD Scores"
    )

    gr.Markdown("## Assistant Response")

    response = gr.Textbox(
        label="AI Assistant Response"
    )

    btn.click(
        process_audio,
        inputs=audio_input,
        outputs=[
            speaker1,
            speaker2,
            primary,
            response,
            pud_scores
        ]
    )

demo.launch()