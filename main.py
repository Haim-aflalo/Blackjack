from core import deck,game_logic,player_io

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:

    game_logic.deal_two_each(deck,player,dealer)
