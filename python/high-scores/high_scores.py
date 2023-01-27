def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = scores[0]
    for i in range(len(scores)):
        if scores[i] > best:
            best = scores[i]
    return best
        
def personal_top_three(scores):
    sorted = scores.copy()
    sorted.sort(reverse = True)
    top = sorted[0:3]
    return top
