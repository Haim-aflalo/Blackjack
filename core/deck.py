import random

def build_standard_deck() -> list[dict]:
    deck = []
    color = ["H","C","D","S"]
    val = ["A","2",'3','4','5','6','7','8','9','10','J','Q','K']
    for i in range(len(color)):
        for j in range(len(val)):
         card = {"rank": val[j], "suite": color[i]}
         deck.append(card)
    return deck


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    while swaps:
        i = random.choice(range(0,52))
        while True:
            j = random.choice(range(0,52))
            if i == j:
                j = random.choice(range(0, 52))
            if deck[i]["suite"] == "H" and j % 5 != 0:
                continue
            if deck[i]["suite"] == "C" and j % 3 != 0:
                continue
            if deck[i]["suite"] == "D" and j % 2 != 0:
                continue
            if deck[i]["suite"] == "S" and j % 7 != 0:
                continue
            else:
                break
        swaps -= 1
        deck[i],deck[j] = deck[j],deck[i]
    return deck


