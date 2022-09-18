import pygame ,sys 
import numpy as np
pygame.init()

width = 700
height = 700
line_width = 15
win_line_width = 15
board_rows = 3
board_cols = 3
square_size = 235
cross_width = 25
space = 55

#colours
bg_colour = (20, 200, 160)
line_colour = (0, 0, 0)
circle_colour = (0, 255, 0)
cross_colour = (255, 0, 0)

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Tic Tac Toe")
screen.fill(bg_colour)

# Using numpy grid to create the board.
board = np.zeros((board_rows, board_cols))

def draw_lines():
    pygame.draw.line(screen, line_colour, (0, square_size), (width, square_size), line_width)
    pygame.draw.line(screen, line_colour, (0, 2 * square_size), (width, 2 * square_size), line_width)
    pygame.draw.line(screen, line_colour, (square_size, 0), (square_size, height), line_width)
    pygame.draw.line(screen, line_colour, (2 * square_size, 0), (2 * square_size, height), line_width)

def draw_figures():
    for row in range(board_rows) :
        for col in range(board_cols) : 
            if board[row][col] == 1:
                pygame.draw.circle(screen , circle_colour, (int(col * square_size + square_size//2), int(row * square_size + square_size//2)), 60, 15)
            elif board[row][col] == 2:
                pygame.draw.line( screen, cross_colour, (col * square_size + space, row * square_size + square_size - space), (col * square_size + square_size - space, row * square_size + space), cross_width)
                pygame.draw.line( screen, cross_colour, (col * square_size + space, row * square_size + space), (col * square_size + square_size - space, row * square_size + square_size - space), cross_width)

def mark_square(row, col, player):
    board[row][col] = player

def available_squares(row, col):
    return board[row][col] == 0

def board_full():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True

def draw_vertical_winning_line(col, player):
    posX = col * square_size + square_size//2
    
    if player == 1:
        color = circle_colour
    elif player == 2:
        color = cross_colour
    pygame.draw.line(screen, color, (posX, 15), (posX, height - 15), win_line_width)

def draw_horizontal_winning_line(row, player):
    posY = row * square_size + square_size//2

    if player == 1:
        color = circle_colour
    if player == 2:
        color = cross_colour
    pygame.draw.line(screen, color, (15, posY), (width - 15, posY), win_line_width)

def draw_asc_diagonal_line(player):
    if player == 1:
        color = circle_colour
    if player == 2:
        color = cross_colour

    pygame.draw.line(screen, color, (15, height - 15), (width - 15, 15), win_line_width)

def draw_desc_diagonal_line(player):
    if player == 1:
        color = circle_colour
    if player == 2:
        color = cross_colour

    pygame.draw.line(screen, color, (15, 15), (width - 15, height - 15), win_line_width)

def check_win(player):
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            draw_vertical_winning_line(col, player)
            return True
    
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row, player)
            return True

    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        draw_asc_diagonal_line(player)
        return True
    
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal_line(player)
        return True

def restart():
    screen.fill(bg_colour)
    draw_lines()
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

draw_lines()

player = 1
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX = event.pos[0]
            mouseY = event.pos[1]

            clicked_row = int(mouseY // square_size)
            clicked_col = int(mouseX // square_size)
        
            if available_squares( clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                if check_win(player):
                    game_over = True
                player = player % 2 + 1
    
                draw_figures()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
                player == 1
                game_over = False
                
    pygame.display.update()
