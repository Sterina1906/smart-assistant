import pandas as pd
from jiwer import wer

results = []

def log_result(file_name, ref_text, pred_text, sisnr):

    error = wer(ref_text, pred_text)

    results.append({
        "file": file_name,
        "WER": round(error, 3),
        "SI-SNR": round(sisnr, 2)
    })

def save_results():

    df = pd.DataFrame(results)

    df.to_csv("outputs/results/evaluation.csv", index=False)

    print(df)