from core import deck,game_logic,player_io



def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    game_logic.deal_two_each(deck,player,dealer)
    choice_player= player_io.ask_player_action()
    while choice_player == "H":
        player_hand = 0
        new_card = player["hand"].append(deck.pop(0))
        player_hand = game_logic.calculate_hand_value(player["hand"])
        if player_hand > 21:
            print("THE PLAYER LOOSE!!!")
            break
        else:
            continue

    if choice_player == "S":
        if game_logic.dealer_play(deck,dealer):
            pl_hand = game_logic.calculate_hand_value(player["hand"])
            dl_hand = game_logic.calculate_hand_value(dealer["hand"])
            if pl_hand > dl_hand:
                print("THE PLAYER WON")
                return
            if pl_hand < dl_hand:
                print("THE DEALER WON")
                return
            else:
                print(f"player:{pl_hand} dealer:{dl_hand}")
                return



if __name__ == "__main__":
    game_deck = deck.build_standard_deck()
    shuffle = deck.shuffle_by_suit(game_deck)
    player = {"hand":[]}
    dealer = {"hand":[]}
    run_full_game(shuffle,player,dealer)