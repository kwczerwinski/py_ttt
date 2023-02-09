from itertools import cycle as itertools_cycle
from ttt_enums import GameState, GridState, StatusCode
from ttt_grid import grid_start, check_grid_state
from ttt_players import players, set_players_name
from ttt_user_inputs import get_move_from_user, get_rounds_from_user
from ttt_utilities import exit_on_failure, conclude_game


def play_game() -> tuple[StatusCode, list[str]]:
    status_code = StatusCode.SUCCESS
    grid = grid_start[:]
    game_state = GameState.START
    set_players_name()
    players_iter = itertools_cycle(players)

    while game_state != GameState.END:
        game_state = GameState.IN_PROGRESS
        player = next(players_iter)
        move = get_move_from_user(player, grid)
        grid[move] = player.sign.value
        grid_state = check_grid_state(grid)

        if grid_state == GridState.NOT_CONCLUDED:
            continue
        elif grid_state == GridState.WINNER:
            player.wins += 1

        game_state = GameState.END

    return (status_code, grid)


if __name__ == "__main__":
    status_code, rounds = get_rounds_from_user()
    exit_on_failure(status_code)
    for _ in range(rounds):
        status_code, grid = play_game()
        exit_on_failure(status_code)
        conclude_game(players, grid)
