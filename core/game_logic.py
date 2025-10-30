from core.deck import build_standard_deck


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


def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    first_p1,second_p1 = deck.pop(0),deck.pop(0)
    first_p2,second_p2 = deck.pop(0),deck.pop(0)
    player["hand"].append(first_p1)
    player["hand"].append(second_p1)
    dealer["hand"].append(first_p2)
    dealer["hand"].append(second_p2)
    player_hand = calculate_hand_value(player["hand"])
    dealer_hand = calculate_hand_value(dealer["hand"])
    print(player_hand,dealer_hand)

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    score = 0
    while True:
        dealer_card = deck.pop(0)
        score += calculate_hand_value([dealer_card])
        if score <= 17:
            print("a")
            continue
        if score > 21:
            print("the dealer loose")
            return False
        if 18 < score < 21:
            print(2)
            return True

