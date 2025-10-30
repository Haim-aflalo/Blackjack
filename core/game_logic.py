def calculate_hand_value(hand: list[dict]) -> int:
    hand_points = 0
    val = {"A":1,"J":10,"Q":10,"K":10}
    for i in range(len(hand)):
        card = hand[i]["rank"]
        if hand[i]["rank"].isdigit():
            hand_points+=int(hand[i]["rank"])
        else:
            hand_points += val[card]
    return hand_points



