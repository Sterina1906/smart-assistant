import pandas as pd
from jiwer import wer

results = []

def evaluate(file, ref, hyp):

    error = wer(ref, hyp)

    results.append({
        "file": file,
        "WER": round(error, 3)
    })


def save():

    df = pd.DataFrame(results)
    df.to_csv("outputs/results/evaluation.csv", index=False)

    print(df)