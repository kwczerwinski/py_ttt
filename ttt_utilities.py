from ttt_enums import StatusCode
from ttt_grid import show_grid
from ttt_players import Player, show_players_board


def clear_terminal() -> None:
    print("\033c", end="")


def conclude_game(players: list[Player], grid: list[str]) -> None:
    show_game(players, grid)
    players = sorted(players, key=lambda p: p.wins, reverse=True)
    if all(player.wins == players[0].wins for player in players):
        print("Draw!")
    else:
        print(f"{players[0].name} wins!")


def exit_on_failure(status_code):
    if status_code == StatusCode.FAILURE:
        exit()


def show_game(players: list[Player], grid: list[str]) -> None:
    clear_terminal()
    show_players_board(players)
    show_grid(grid)
