import random

def drawGrid(grid):
    """
    Draw 2048 grid
    """
    for row in grid:
        print('|'.join(f'{cell:4}' for cell in row))

def transpose_grid(grid):
    """
    Transpose grid by swaping the columns with rows
    
    Before transpose:

    [[4,  2,  0, 0], 
     [16, 0,  0, 0], 
     [2,  16, 0, 0], 
     [16, 32, 2, 0]]

    After transpose:

    [[4, 16, 2, 16], 
     [2, 0, 16, 32], 
     [0, 0, 0,   2], 
     [0, 0, 0,  0 ]]

    Usage:

    >>> grid = [[4,  2,  0, 0], [16, 0,  0, 0], [2,  16, 0, 0], [16, 32, 2, 0]]
    >>> transpose_grid(grid)
    [[4, 16, 2, 16], [2, 0, 16, 32], [0, 0, 0, 2], [0, 0, 0, 0]]
    """

    transposed_grid = list(map(list, zip(*grid)))
    return transposed_grid

def initial_random(grid):
    '''
    Set up the initial board position in the beginning of the game.

    [[0, 2, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 0, 0],
     [0, 0, 2, 0]]

    Two cells get randomly initialized with the value of 2 or 4.
    There's a 90% chance of getting 2.

    Usage:

    >>> grid = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, 0]]
    >>> random.seed(2048)
    >>> initial_random(grid)
    [[0, 0, 0, 0], [0, 0, 0, 2], [0, 2, 0, 0], [0, 0, 0, 0]]
    '''
    positions = random.sample(range(16), 2)  # Generate 2 unique positions
    
    for pos in positions:
        i = pos // 4  # Convert position to row index
        j = pos % 4  # Convert position to column index
        grid[i][j] = random.choices([2, 4], weights=[0.9, 0.1])[0]  # Weighted random choice
    
    return grid

def move_trailing_zeros_to_the_right(lst):
    """
    Takes in a list and moves all zeroes in the list to the right.

    input:
    
    [4, 0, 4, 0]

    output:

    [0, 0, 4, 4]

    Usage:

    >>> move_trailing_zeros_to_the_right([4, 0, 4, 0])
    [0, 0, 4, 4]
    """

    num_zeros = lst.count(0)  # Count the number of zeros in the list
    lst = [0] * num_zeros + [num for num in lst if num != 0]
    return lst

def move_trailing_zeros_to_the_left(lst):
    """
    Takes in a list and moves all zeroes in the list to the left.

    input:
    
    [2, 0, 2, 0]

    output:

    [2, 2, 0, 0]

    Usage:

    >>> move_trailing_zeros_to_the_left([2, 0, 2, 0])
    [2, 2, 0, 0]
    """

    num_zeros = lst.count(0)  # Count the number of zeros in the list
    lst = [num for num in lst if num != 0] + [0] * num_zeros
    return lst

def move_right(grid):
    """
    Move all numbers to the right of the grid and adds them if they are the same.

    Before moving right:

    [[0, 0, 0, 0], 
     [4, 4, 0, 0], 
     [8, 0, 0, 0], 
     [8, 8, 0, 0]]
    
    After moving right:

    [[0, 0, 0, 0], 
     [0, 0, 0, 8], 
     [0, 0, 0, 8], 
     [0, 0, 0, 16]]

    Usage:

    >>> move_right([[0, 0, 0, 0], [4, 4, 0, 0], [8, 0, 0, 0], [8, 8, 0, 0]])
    [[0, 0, 0, 0], [0, 0, 0, 8], [0, 0, 0, 8], [0, 0, 0, 16]]
    """

    for i in range(4):
        grid[i] = move_trailing_zeros_to_the_right(grid[i])
        for j in range(3):
            if grid[i][j] == 0:
                continue
            else:
                if grid[i][j] == grid[i][j+1]:
                    grid[i][j+1] = grid[i][j] + grid[i][j+1]
                    grid[i][j] = 0

    return grid
                    
def move_left(grid):
    """
    Move all numbers to the left of the grid and adds them if they are the same.

    Before moving left:
    
    [[4, 0, 0, 0], 
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [2, 2, 0, 0]]
    
    After moving left:

    [[4, 0, 0, 0],
     [0, 0, 0, 0], 
     [0, 0, 0, 0], 
     [4, 0, 0, 0]]

    Usage:

    >>> move_left([[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 2, 0, 0]])
    [[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [4, 0, 0, 0]]

    """

    for i in range(4):
        grid[i] = move_trailing_zeros_to_the_right(grid[i])
        for j in range(3):
            if grid[i][j] == 0:
                continue
            else:
                if grid[i][j] == grid[i][j+1]:
                    grid[i][j+1] = grid[i][j] + grid[i][j+1]
                    grid[i][j] = 0

        grid[i] = move_trailing_zeros_to_the_left(grid[i])
    
    return grid

def check_loss(grid):
    """
    Check if the player has lost the game

    Args:
        grid (list): The game grid.

    Returns:
        bool: True if the player has lost, False otherwise.

    >>> grid = [[4, 2, 0, 0], [16, 0, 0, 0], [2, 16, 0, 0], [16, 32, 2, 0]]
    >>> check_loss(grid)
    False

    >>> grid = [[4, 2, 4, 8], [16, 32, 64, 128], [2, 4, 8, 16], [64, 32, 16, 8]]
    >>> check_loss(grid)
    True

    >>> grid = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]]
    >>> check_loss(grid)
    True

    >>> grid = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 2, 128]]
    >>> check_loss(grid)
    True

    >>> grid = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 2, 2, 128]]
    >>> check_loss(grid)
    False

    >>> grid = [[4, 4, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128], [32, 64, 128, 256]]
    >>> check_loss(grid)
    False
    """
    
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False  # Empty cell found, the game can continue

    for i in range(4):
        if grid[i][0] == grid[i][1] or grid[i][1] == grid[i][2] or grid[i][2]  == grid[i][3]:
            return False

    grid = transpose_grid(grid)

    for i in range(4):
        if grid[i][0] == grid[i][1] or grid[i][1] == grid[i][2] or grid[i][2]  == grid[i][3]:
            return False

    return True

def check_2048(grid):
    """
    Check if the player has gotten 2048

    Args:
        grid (list): The game grid.

    Returns:
        bool: True if the player has gotten 2048 and None if they haven't
    
    >>> grid = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]]
    >>> check_2048(grid)
    False

    >>> grid = [[2, 4, 8, 16], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 2048]]
    >>> check_2048(grid)
    True

    >>> grid = [[1024, 2, 4, 8], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 128]]
    >>> check_2048(grid)
    False

    >>> grid = [[1024, 2, 4, 8], [4, 8, 16, 32], [8, 16, 32, 64], [16, 32, 64, 2048]]
    >>> check_2048(grid)
    True
    """

    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
    
    return False

if __name__ == "__main__":
    import doctest
    doctest.testmod()
