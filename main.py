# Display grid
# Handle player moves
# Track game state
# Check for win or draw
# Multiple rounds

from enum import IntEnum

class StatusCode(IntEnum):
	SUCCESS = 0,
	FAILURE = 1

grid_start = [
	'...',
	'...',
	'...'
]

def display_grid(grid):
	[ print(row) for row in grid ]

def get_rounds_from_user():
	status_code = StatusCode.SUCCESS
	user_input = 0
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

if __name__ == "__main__":
	status_code, rounds = get_rounds_from_user()
	if status_code == StatusCode.FAILURE:
		exit()
	for _ in range(rounds):
		clear_terminal()
		display_grid(grid_start)