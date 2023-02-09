from ttt_enums import GridState


grid_start = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def check_grid_state(grid: list[str]) -> GridState:
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


def possible_values_from_grid(grid: list[str]) -> list[int]:
    values = []

    for i in grid:
        try:
            values.append(int(i))
        except ValueError:
            pass

    return values


def show_grid(grid: list[str]) -> None:
    for i in range(0, len(grid), 3):
        print(grid[i:i+3])
    print()
