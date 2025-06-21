import pygame

pygame.init()
W, H = 600, 700
SQ = W // 3
IMG_SIZE = int(SQ * 0.8)
IMG_OFFSET = (SQ - IMG_SIZE) // 2
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Tic Tac Toe")

X = pygame.transform.scale(pygame.image.load("x.png"), (IMG_SIZE, IMG_SIZE))
O = pygame.transform.scale(pygame.image.load("circle.png"), (IMG_SIZE, IMG_SIZE))

B = [[None]*3 for _ in range(3)]
P = "X"
winner = None
line_coords = None
font = pygame.font.SysFont(None, 60)
popup_font = pygame.font.SysFont(None, 70)

def draw_lines():
    for i in range(1, 3):
        pygame.draw.line(screen, (0, 0, 0), (0, i*SQ), (W, i*SQ), 5)
        pygame.draw.line(screen, (0, 0, 0), (i*SQ, 0), (i*SQ, SQ*3), 5)

def draw_figures():
    for r in range(3):
        for c in range(3):
            if B[r][c] == "X":
                screen.blit(X, (c*SQ + IMG_OFFSET, r*SQ + IMG_OFFSET))
            elif B[r][c] == "O":
                screen.blit(O, (c*SQ + IMG_OFFSET, r*SQ + IMG_OFFSET))

def check():
    global winner, line_coords
    for i in range(3):
        if B[i][0] == B[i][1] == B[i][2] and B[i][0]:
            winner = B[i][0]
            line_coords = ((0, i*SQ + SQ//2), (W, i*SQ + SQ//2))
        if B[0][i] == B[1][i] == B[2][i] and B[0][i]:
            winner = B[0][i]
            line_coords = ((i*SQ + SQ//2, 0), (i*SQ + SQ//2, SQ*3))
    if B[0][0] == B[1][1] == B[2][2] and B[0][0]:
        winner = B[0][0]
        line_coords = ((0, 0), (W, SQ*3))
    if B[0][2] == B[1][1] == B[2][0] and B[0][2]:
        winner = B[0][2]
        line_coords = ((W, 0), (0, SQ*3))

def draw_popup():
    if winner:
        box_rect = pygame.Rect(W//2 - 200, H//2 - 100, 400, 200)
        pygame.draw.rect(screen, (255, 255, 255), box_rect)
        pygame.draw.rect(screen, (0, 0, 0), box_rect, 4)
        text = popup_font.render(f"{winner} Wins!", True, (0, 128, 0))
        screen.blit(text, (box_rect.centerx - text.get_width()//2, box_rect.centery - text.get_height()//2))

def reset():
    global B, P, winner, line_coords
    B = [[None]*3 for _ in range(3)]
    P = "X"
    winner = None
    line_coords = None
    screen.fill((255, 255, 255))
    draw_lines()
    draw_button()

def draw_button():
    btn_rect = pygame.Rect(W//2 - 80, H - 60, 160, 40)
    pygame.draw.rect(screen, (255, 255, 255), btn_rect)
    pygame.draw.rect(screen, (0, 0, 0), btn_rect, 2)
    text = font.render("Reset", True, (0, 0, 0))
    screen.blit(text, (btn_rect.centerx - text.get_width()//2, btn_rect.centery - text.get_height()//2))
    return btn_rect

screen.fill((255, 255, 255))
draw_lines()
btn_rect = draw_button()
run = True

while run:
    draw_figures()
    if winner:
        pygame.draw.line(screen, (255, 0, 0), line_coords[0], line_coords[1], 10)
        draw_popup()
    pygame.display.flip()
    check()

    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if btn_rect.collidepoint(x, y):
                reset()
                btn_rect = draw_button()
            elif y < SQ*3 and not winner:
                r, c = y // SQ, x // SQ
                if B[r][c] is None:
                    B[r][c] = P
                    P = "O" if P == "X" else "X"
