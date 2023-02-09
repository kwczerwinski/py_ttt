from ttt_enums import Sign


class Player:
    def __init__(self, sign, name):
        self.sign = sign
        self.name = name
        self.wins = 0

    def repr_points(self) -> str:
        return f"{self.name} : {self.wins}"

    def change_name(self) -> None:
        user_input = input(f"Type new player name [{self.name}]:")
        if user_input:
            self.name = user_input


players = [Player(Sign.O, 'Player 1'), Player(Sign.X, 'Player 2')]


def set_players_name() -> None:
    for player in players:
        player.change_name()


def show_players_board(players: list[Player]) -> None:
    print([player.repr_points() for player in players])
    print()
