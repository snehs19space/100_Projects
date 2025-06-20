import pygame

pygame.init()
WIDTH, HEIGHT = 600, 600
LINE_WIDTH = 15
ROWS, COLS = 3, 3
SQ_SIZE = WIDTH // COLS
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
x_img = pygame.image.load("x.png")
o_img = pygame.image.load("circle.png")
x_img = pygame.transform.scale(x_img, (SQ_SIZE, SQ_SIZE))
o_img = pygame.transform.scale(o_img, (SQ_SIZE, SQ_SIZE))
board = [[None] * COLS for _ in range(ROWS)]
current = "X"
winner = None

def draw_lines():
    for i in range(1, ROWS):
        pygame.draw.line(screen, LINE_COLOR, (0, i*SQ_SIZE), (WIDTH, i*SQ_SIZE), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (i*SQ_SIZE, 0), (i*SQ_SIZE, HEIGHT), LINE_WIDTH)

def draw_board():
    for row in range(ROWS):
        for col in range(COLS):
            val = board[row][col]
            if val == "X":
                screen.blit(x_img, (col*SQ_SIZE, row*SQ_SIZE))
            elif val == "O":
                screen.blit(o_img, (col*SQ_SIZE, row*SQ_SIZE))

def check_winner():
    global winner
    for i in range(ROWS):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0]:
            winner = board[i][0]
    for i in range(COLS):
        if board[0][i] == board[1][i] == board[2][i] and board[0][i]:
            winner = board[0][i]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0]:
        winner = board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2]:
        winner = board[0][2]

def restart():
    global board, current, winner
    board = [[None] * COLS for _ in range(ROWS)]
    current = "X"
    winner = None
    screen.fill(BG_COLOR)
    draw_lines()

screen.fill(BG_COLOR)
draw_lines()
running = True

while running:
    draw_board()
    pygame.display.flip()
    check_winner()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and not winner:
            mx, my = pygame.mouse.get_pos()
            row = my // SQ_SIZE
            col = mx // SQ_SIZE
            if board[row][col] is None:
                board[row][col] = current
                current = "O" if current == "X" else "X"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()

