import os
import numpy as np
import soundfile as sf

os.makedirs("data/synthetic", exist_ok=True)

sr = 16000

def generate_noise(duration=2):
    return np.random.normal(0, 0.02, sr * duration)

def generate_signal(freq=200):
    t = np.linspace(0, 2, sr * 2)
    return 0.1 * np.sin(2 * np.pi * freq * t)

count = 0

for i in range(10):
    for j in range(2):

        s1 = generate_signal(200 + i * 10)
        s2 = generate_noise()

        mix = s1[:len(s2)] + s2

        sf.write(f"data/synthetic/mix_{count}.wav", mix, sr)

        print("Created:", count)

        count += 1

print("20 synthetic clips ready")