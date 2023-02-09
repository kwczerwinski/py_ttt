from enum import IntEnum, StrEnum
import itertools


class StatusCode(IntEnum):
    SUCCESS = 0,
    FAILURE = 1


class GameState(IntEnum):
    START = 0,
    IN_PROGRESS = 1,
    END = 2


class Turn(IntEnum):
    PLAYER_1 = 0,
    PLAYER_2 = 1


class Sign(StrEnum):
    O = 'O',
    X = 'X'


def show_grid(grid: list[str]) -> None:
    for i in range(0, len(grid), 3):
        print(grid[i:i+3])
    print()


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


def clear_terminal():
    print("\033c", end="")


class Player:
    def __init__(self, sign, name):
        self.sign = sign
        self.name = name
        self.wins = 0

    def repr_points(self):
        return f"{self.name} : {self.wins}"

    def change_name(self):
        user_input = input(f"Type new player name [{self.name}]:")
        if user_input:
            self.name = user_input


def possible_values_from_grid(grid):
    values = []

    for i in grid:
        try:
            values.append(int(i))
        except ValueError:
            pass

    return values


def show_game(players, grid) -> None:
    clear_terminal()
    show_players_board(players)
    show_grid(grid)


def get_move_from_user(player: Player, grid):
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


class GridState(IntEnum):
    NOT_CONCLUDED = 0,
    WINNER = 1,
    DRAW = 2


def check_grid_state(grid) -> GridState:
    if not possible_values_from_grid(grid):
        return GridState.DRAW

    for i in range(0, len(grid), 3):
        if grid[i] == grid[i+1] and grid[i] == grid[i+2]:
            return GridState.WINNER

    for i in range(3):
        if grid[i] == grid[i+3] and grid[i] == grid[i+6]:
            return GridState.WINNER

    if grid[0] == grid[4] and grid[0] == grid[8]:
        return GridState.WINNER

    if grid[2] == grid[4] and grid[2] == grid[6]:
        return GridState.WINNER

    return GridState.NOT_CONCLUDED


def show_players_board(players: list[Player]) -> None:
    print([player.repr_points() for player in players])
    print()


def conclude_game(players: list[Player]) -> None:
    players = sorted(players, key=lambda p: p.wins, reverse=True)
    if all(player.wins == players[0].wins for player in players):
        print("Draw!")
    else:
        print(f"{players[0].name} wins!")


grid_start = [chr(i) for i in range(ord('1'), ord('9')+1)]
players = [Player(Sign.O, 'Player 1'), Player(Sign.X, 'Player 2')]


def set_players_name() -> None:
    for player in players:
        player.change_name()


def play_game():
    status_code = StatusCode.SUCCESS
    grid = grid_start[:]
    game_state = GameState.START
    set_players_name()
    players_iter = itertools.cycle(players)

    while game_state != GameState.END:
        game_state = GameState.IN_PROGRESS
        player = next(players_iter)
        move = get_move_from_user(player, grid)
        grid[move] = player.sign.value
        grid_state = check_grid_state(grid)

        if grid_state == GridState.NOT_CONCLUDED:
            continue
        else:
            show_game(players, grid)

            if grid_state == GridState.WINNER:
                player.wins += 1

        show_game(players, grid)
        conclude_game(players)
        game_state = GameState.END

    return status_code


def exit_on_failure(status_code):
    if status_code == StatusCode.FAILURE:
        exit()


if __name__ == "__main__":
    status_code, rounds = get_rounds_from_user()
    exit_on_failure(status_code)
    for _ in range(rounds):
        status_code = play_game()
        exit_on_failure(status_code)
