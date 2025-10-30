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
    player["first"],player["second"] = first_p1,second_p1
    dealer["first"],dealer["second"] = first_p2,second_p2
    player_hand = calculate_hand_value([player["first"],player["second"]])
    dealer_hand = calculate_hand_value([dealer["first"], dealer["second"]])
    print(player_hand,dealer_hand)




