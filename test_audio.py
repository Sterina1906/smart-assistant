import librosa

audio, sr = librosa.load("data/mixed/8842-302201-0004_3081-166546-0028.wav", sr=None)

print("Sample Rate:", sr)
print("Audio Length:", len(audio)/sr, "seconds")