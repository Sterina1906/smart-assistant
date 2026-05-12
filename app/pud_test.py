import numpy as np

def compute_pud_score(keyword_flag, energy_score, history_score):
    """
    Primary User Detection Score
    """

    w1, w2, w3 = 0.5, 0.3, 0.2

    score = (
        w1 * energy_score +
        w2 * keyword_flag +
        w3 * history_score
    )

    return round(score, 3)


def detect_primary_user(scores_dict):
    """
    scores_dict = {
        "speaker1": {...},
        "speaker2": {...}
    }
    """

    best_user = None
    best_score = -1

    for user, vals in scores_dict.items():

        score = compute_pud_score(
            vals["keyword"],
            vals["energy"],
            vals["history"]
        )

        if score > best_score:
            best_score = score
            best_user = user

    return best_user, best_score