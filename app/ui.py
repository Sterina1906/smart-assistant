import gradio as gr
import pandas as pd
from pud_test import detect_primary_user

def process_audio(audio):

    transcript_1 = "turn on lights"
    transcript_2 = "random background speech"

    scores = {
        "speaker1": {
            "keyword": 1,
            "energy": 0.9,
            "history": 0.7
        },
        "speaker2": {
            "keyword": 0,
            "energy": 0.4,
            "history": 0.5
        }
    }

    primary_user, score = detect_primary_user(scores)

    response = "Lights turned on in bedroom."

    return (
        transcript_1,
        transcript_2,
        primary_user,
        score,
        response
    )


def load_metrics():

    df = pd.read_csv("outputs/results/evaluation.csv")
    return df


with gr.Blocks() as demo:

    gr.Markdown("# 🧠 Smart Multi-User Assistant")

    audio = gr.Audio(type="filepath")

    btn = gr.Button("Run Pipeline")

    gr.Markdown("## Transcriptions")

    t1 = gr.Textbox(label="Speaker 1")
    t2 = gr.Textbox(label="Speaker 2")

    gr.Markdown("## Primary User Detection")

    primary = gr.Textbox(label="Primary User")
    score = gr.Number(label="PUD Score")

    gr.Markdown("## Response")

    response = gr.Textbox(label="Assistant Response")

    gr.Markdown("## Evaluation Results")

    table = gr.Dataframe()

    metrics_btn = gr.Button("Load Evaluation CSV")

    btn.click(
        process_audio,
        inputs=audio,
        outputs=[t1, t2, primary, score, response]
    )

    metrics_btn.click(
        load_metrics,
        inputs=[],
        outputs=table
    )

demo.launch()