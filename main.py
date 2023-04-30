import random
import copy
import pygame
import sys

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
BLUE = (0, 0, 255)

# Initialize Pygame
pygame.init()

# Set the window size
WINDOW_SIZE = (550, 550)

# Set the font for the numbers
FONT = pygame.font.SysFont('calibri', 40)

# Create the window
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set the title of the window
pygame.display.set_caption('Sudoku')

# Generate a blank Sudoku board
def generate_board():
    
    board = [[0 for _ in range(9)] for _ in range(9)]
    return board

# Fill the board with random valid numbers
def fill_board(board):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    random.shuffle(numbers)
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                random.shuffle(numbers)
                for num in numbers:
                    if is_valid(num, row, col, board):
                        board[row][col] = num
                        if fill_board(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Generate a solvable Sudoku puzzle with a unique solution
def generate_puzzle(board, difficulty):
    """
    Creates a puzzle by removing numbers from the board based on the specified difficulty level.
    """
    if difficulty == "easy":
        # Remove 40 numbers from the board
        remove_count = 40
    elif difficulty == "medium":
        # Remove 45 numbers from the board
        remove_count = 50
    else:
        # Remove 50 numbers from the board
        remove_count = 60
    
    board = generate_board()
    fill_board(board)
   
    # Create a copy of the board
    puzzle = [row[:] for row in board]
    # Randomly remove numbers from the board until the desired difficulty level is reached
    while remove_count > 0:
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        if puzzle[row][col] != 0:
            puzzle[row][col] = 0
            remove_count -= 1

    return puzzle

# Check if a number is valid for a given row, column, or sub-grid
def is_valid(num, row, col, board):
    # Check the row
    if num in board[row]:
        return False
    # Check the column
    for i in range(9):
        if num == board[i][col]:
            return False
    # Check the sub-grid
    sub_row = (row // 3) * 3
    sub_col = (col // 3) * 3
    for i in range(sub_row, sub_row + 3):
        for j in range(sub_col, sub_col + 3):
            if num == board[i][j]:
                return False
    return True

# Check if a board has a unique solution
def has_unique_solution(board):
    # Make a copy of the board to avoid modifying the original
    board_copy = copy.deepcopy(board)
    # Find the first empty cell
    row, col = find_empty_cell(board_copy)
    # If there are no empty cells, the board is solved
    if row is None:
        return True
    # Try each possible number for the empty cell
    for num in range(1, 10):
        if is_valid(num, row, col, board_copy):
            board_copy[row][col] = num
            # If there is a unique solution for the board with the current number in the empty cell, return True
            
            if has_unique_solution(board_copy):
                return True
            # Otherwise, backtrack and try the next number
            board_copy[row][col] = 0
    # If none of the possible numbers for the empty cell lead to a unique solution, return False
    return False

# Find the first empty cell in a board (represented by 0)
def find_empty_cell(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return row, col
    return None, None

# Check if the board is complete
def is_complete(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return False
    return True
    

# Draw the Sudoku board on the screen
def draw_board(board):
    # Clear the screen
    screen.fill(WHITE)
    
    # Draw the grid lines
    for i in range(10):
        if i % 3 == 0:
            thickness = 4
        else:
            thickness = 1
        pygame.draw.line(screen, BLACK, (50 + i * 50, 50), (50 + i * 50, 500), thickness)
        pygame.draw.line(screen, BLACK, (50, 50 + i * 50), (500, 50 + i * 50), thickness)
    # Draw the numbers
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                num_surface = FONT.render(str(board[row][col]), True, BLACK)
                screen.blit(num_surface, (65 + col * 50, 55 + row * 50))
              

# Main function
def main():
    # Generate a puzzle
    board = generate_puzzle("", "easy")
    # Set the current cell to the top-left corner of the board
    current_row = 0
    current_col = 0
    # Draw the board
    draw_board(board)
    
    # Loop until the user quits
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_row = max(current_row - 1, 0)
                elif event.key == pygame.K_DOWN:
                    current_row = min(current_row + 1, 8)
                elif event.key == pygame.K_LEFT:
                    current_col = max(current_col - 1, 0)
                elif event.key == pygame.K_RIGHT:
                    current_col = min(current_col + 1, 8)
                elif event.key == pygame.K_1:
                    if is_valid(1, current_row, current_col, board):
                        board[current_row][current_col] = 1
                elif event.key == pygame.K_2:
                    if is_valid(2, current_row, current_col, board):
                        board[current_row][current_col] = 2
                elif event.key == pygame.K_3:
                    if is_valid(3, current_row, current_col, board):
                        board[current_row][current_col] = 3
                elif event.key == pygame.K_4:
                    if is_valid(4, current_row, current_col, board):
                        board[current_row][current_col] = 4
                elif event.key == pygame.K_5:
                    if is_valid(5, current_row, current_col, board):
                        board[current_row][current_col] = 5
                elif event.key == pygame.K_6:
                    if is_valid(6, current_row, current_col, board):
                        board[current_row][current_col] = 6
                elif event.key == pygame.K_7:
                    if is_valid(7, current_row, current_col, board):
                        board[current_row][current_col] = 7
                elif event.key == pygame.K_8:
                    if is_valid(8, current_row, current_col, board):
                        board[current_row][current_col] = 8
                elif event.key == pygame.K_9:
                    if is_valid(9, current_row, current_col, board):
                        board[current_row][current_col] = 9
                elif event.key == pygame.K_DELETE or event.key == pygame.K_BACKSPACE:
                    board[current_row][current_col] = 0
                if is_complete(board):
                  draw_board(board)
                  pygame.display.update()
                  pygame.time.wait(1000)
                  # Display a message indicating success
                  font = pygame.font.Font(None, 36)
                  text = font.render("Congratulations, you solved the puzzle!", True, (0, 255, 0))
                  text_rect = text.get_rect()
                  text_rect.center = (250, 525)
                  screen.blit(text, text_rect)
                  pygame.display.update()
                  pygame.time.wait(5000)
        # Draw the board
        draw_board(board)
        # Highlight the current cell
        pygame.draw.rect(screen, BLUE, (50 + current_col * 50, 50 + current_row * 50, 50, 50), 3)
        # Update the display
        pygame.display.update()

# Run the main function
if __name__ == '__main__':
    main()
