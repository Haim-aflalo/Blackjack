def build_standard_deck() -> list[dict]:
    deck = []
    color = ["H","C","D","S"]
    val = ["A","2",'3','4','5','6','7','8','9','10','J','Q','K']
    for i in range(len(color)):
        for j in range(len(val)):
            card = {"rank": val[j], "suite": color[i]}
            deck.append(card)
    return deck

