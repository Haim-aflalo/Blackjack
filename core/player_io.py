def ask_player_action() -> str:
    option = ["H","S"]
    while True:
        action = input("CHOOSE: S for Stand or H for Hit")
        if action not in option:
            print("WRONG CHOICE !")
            continue
        return action
