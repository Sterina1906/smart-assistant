from jiwer import wer
import soundfile as sf
import numpy as np
from mir_eval.separation import bss_eval_sources

def calculate_wer(reference, hypothesis):
    return wer(reference, hypothesis)

def calculate_sisnr(reference_audio, estimated_audio):
    sdr, sir, sar, perm = bss_eval_sources(reference_audio, estimated_audio)
    return np.mean(sdr)

if __name__ == "__main__":

    ref_text = "turn on the kitchen lights"
    pred_text = "turn on kitchen lights"

    print("WER:", calculate_wer(ref_text, pred_text))