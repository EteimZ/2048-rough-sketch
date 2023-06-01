"""
My rough implementation 2048
"""

import random
from utils import (
    initial_random,
    drawGrid,
    transpose_grid,
    move_left,
    move_right,
    check_2048,
    check_loss
)

def main():

    # Create a grid for the game
    grid = [[0, 0, 0, 0] for _ in range(4)]

    # Randomly initialize the grid
    initial_random(grid)

    # Game loop
    while True:
        drawGrid(grid)

        inp = input("Please press key(w⬆️|s⬇️|a⬅️|d➡️|e to exit): ")
        if inp == 'w':
            # transpose the grid
            t_grid = transpose_grid(grid)
            # retranspose the grid after moving left
            grid = transpose_grid(move_left(t_grid))
        elif inp == 's':
            # transpose the grid
            t_grid = transpose_grid(grid)
            # retranspose the grid after moving right
            grid = transpose_grid(move_right(t_grid))
        elif inp == 'a':
            grid = move_left(grid)
        elif inp == 'd':
            grid = move_right(grid)
        elif inp == 'e':
            exit()
        else:
            print("Unknown key has been pressed!")

        if check_2048(grid):
            print("Congrats you got 2048")
    
        if check_loss(grid):
            print("Game over!")
            break
        
        # Ensure only empty get assigned new values
        empty_positions = [(i, j) for i in range(4) for j in range(4) if grid[i][j] == 0]

        if not empty_positions:
            continue  # No empty positions, exit the function

        i, j = random.choice(empty_positions)
        grid[i][j] = random.choice([2, 4])

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        exit()
