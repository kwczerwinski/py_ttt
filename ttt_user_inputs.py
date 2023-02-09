from ttt_enums import StatusCode
from ttt_grid import possible_values_from_grid
from ttt_players import Player, players
from ttt_utilities import clear_terminal, show_game

def get_rounds_from_user() -> tuple[StatusCode, int]:
    status_code = StatusCode.SUCCESS
    user_input = None
    input_prompt = "How many round you want to play? "
    error_prompt = "Invalid value. It should be a positive integer."

    try:
        clear_terminal()
        user_input = int(input(input_prompt))
        if user_input <= 0:
            raise ValueError(user_input)
    except ValueError as e:
        print(error_prompt, e)
        status_code = StatusCode.FAILURE

    return (status_code, user_input)


def get_move_from_user(player: Player, grid: list[str]) -> int:
    user_input = None
    input_prompt = f"Where whould you like to put your sign [{player.sign}]? "
    error_prompt = "Invalid value. Possible values:"

    show_game(players, grid)
    while True:
        try:
            user_input = int(input(input_prompt))
            if user_input < 1 or user_input > 9 or str(user_input) not in grid:
                raise ValueError(user_input)
            break
        except ValueError as e:
            print(error_prompt, possible_values_from_grid(grid))
            print("\033[A", end="")
            print("\033[A", end="")

    return user_input - 1
