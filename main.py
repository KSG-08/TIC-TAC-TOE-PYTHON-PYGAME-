# importing modules
import pygame
import time
import sys


pygame.init()

# global variables
WIDTH, HEIGHT = 450, 450
FPS = 30
CELL_SIZE = WIDTH / 3
CLOCK = pygame.time.Clock()
run = True
# game variables
playing = False
displaying_help_menu = False
board = [['', '', ''],
         ['', '', ''],
         ['', '', '']]
win = False
flag = False
winner = ''
player = 0

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (10, 255, 200)
BLUE = (0, 0, 255)
WATERMARK = (207, 202, 202)
PLAYER_0 = (100, 47, 186)
INSTRUCTION_1 = (187, 201, 143)
PLAYER_1 = (116, 153, 46)
INSTRUCTION_2 = (187, 161, 230)

# setting up main window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")


def renderText(txt, size, color, y=None):
    font = pygame.font.SysFont('Comic Sans', size, True)
    text = font.render(txt, True, color)
    textRect = text.get_rect()
    if y is None:
        textRect.center = (WIDTH // 2, HEIGHT // 2)
        SCREEN.blit(text, textRect)
    else:
        textRect.centerx = WIDTH // 2
        textRect.y = y
        SCREEN.blit(text, textRect)


def menu():
    renderText("TIC TAC TOE", 60, BLACK, 100)
    renderText("Press 'R' key to reset game!", 30, INSTRUCTION_1, 200)
    renderText("Press 'P' key to start game!", 30, INSTRUCTION_1, 250)
    renderText("Press 'Esc' key to quit game!", 30, INSTRUCTION_1, 300)
    renderText("Press 'H' key for Help!", 30, RED, 350)


def help_menu():
    SCREEN.fill(WHITE)

    renderText("CONTROLS!", 60, BLACK, 70)
    renderText("Use numpad to place an", 30, INSTRUCTION_2, 150)
    renderText("'x' or an 'o'", 30, INSTRUCTION_2, 170)
    renderText("in the tic tac toe grid", 30, INSTRUCTION_2, 190)
    renderText("depending on your choice!", 30, INSTRUCTION_2, 210)
    renderText("For instance, the '7' key", 30, RED, 270)
    renderText("would place an 'x' in", 30, RED, 290)
    renderText("the top left corner...", 30, RED, 310)
    renderText("Press 'P' key to start game", 40, INSTRUCTION_2, 350)


def drawO(txt, x, y):
    font = pygame.font.SysFont("Comicsans", 100, False)
    text = font.render(txt, True, PLAYER_0)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    SCREEN.blit(text, textRect)


def drawX(txt, x, y):
    font = pygame.font.SysFont("Comicsans", 100, False)
    text = font.render(txt, True, PLAYER_1)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    SCREEN.blit(text, textRect)


def draw_watermark(txt, x, y):
    font = pygame.font.SysFont("Comicsans", 40, False)
    text = font.render(txt, True, WATERMARK)
    textRect = text.get_rect()
    textRect.centerx = x
    textRect.centery = y
    SCREEN.blit(text, textRect)


def draw():
    global board

    # drawing horizontal lines
    for row in range(3):
        if row == 0 or row == HEIGHT:
            pass
        else:
            pygame.draw.line(SCREEN, BLACK, (0, row * CELL_SIZE), (WIDTH, row * CELL_SIZE), 3)

    # drawing vertical lines
    for column in range(3):
        if column == 0 or column == WIDTH:
            pass
        else:
            pygame.draw.line(SCREEN, BLACK, (column * CELL_SIZE, 0), (column * CELL_SIZE, HEIGHT), 3)

    count = 1
    for x in range(2, -1, -1):
        for y in range(3):
            if board[y][x] == '':
                draw_watermark(str(count), (y * CELL_SIZE + 75), (x * CELL_SIZE + 75))
            count += 1

    # drawing pieces on board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O':
                drawO("O", (i * CELL_SIZE + 75), (j * CELL_SIZE + 75))
            elif board[i][j] == 'X':
                drawX("X", (i * CELL_SIZE + 75), (j * CELL_SIZE + 75))


def handle_key_events():
    global playing, displaying_help_menu, run, player

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False
    elif keys[pygame.K_r]:
        resetGame()
    elif keys[pygame.K_p]:
        draw()
        playing = True
    elif keys[pygame.K_h]:
        if not playing:
            displaying_help_menu = True
        else:
            pass
    elif keys[pygame.K_KP1]:
        if board[0][2] == '':
            if player == 0:
                board[0][2] = 'O'
                player = 1
            else:
                board[0][2] = 'X'
                player = 0
    elif keys[pygame.K_KP2]:
        if board[1][2] == '':
            if player == 0:
                board[1][2] = 'O'
                player = 1
            else:
                board[1][2] = 'X'
                player = 0
    elif keys[pygame.K_KP3]:
        if board[2][2] == '':
            if player == 0:
                board[2][2] = 'O'
                player = 1
            else:
                board[2][2] = 'X'
                player = 0
    elif keys[pygame.K_KP4]:
        if board[0][1] == '':
            if player == 0:
                board[0][1] = 'O'
                player = 1
            else:
                board[0][1] = 'X'
                player = 0
    elif keys[pygame.K_KP5]:
        if board[1][1] == '':
            if player == 0:
                board[1][1] = 'O'
                player = 1
            else:
                board[1][1] = 'X'
                player = 0
    elif keys[pygame.K_KP6]:
        if board[2][1] == '':
            if player == 0:
                board[2][1] = 'O'
                player = 1
            else:
                board[2][1] = 'X'
                player = 0
    elif keys[pygame.K_KP7]:
        if board[0][0] == '':
            if player == 0:
                board[0][0] = 'O'
                player = 1
            else:
                board[0][0] = 'X'
                player = 0
    elif keys[pygame.K_KP8]:
        if board[1][0] == '':
            if player == 0:
                board[1][0] = 'O'
                player = 1
            else:
                board[1][0] = 'X'
                player = 0
    elif keys[pygame.K_KP9]:
        if board[2][0] == '':
            if player == 0:
                board[2][0] = 'O'
                player = 1
            else:
                board[2][0] = 'X'
                player = 0


def resetGame():
    global player, winner, board, win, flag

    player = 0
    winner = ''
    win = False
    flag = False
    board = [['', '', ''],
             ['', '', ''],
             ['', '', '']]


def check_win():
    global winner, win

    x_wins = [board[0][0] == board[1][0] == board[2][0] == 'X',
              board[0][1] == board[1][1] == board[2][1] == 'X',
              board[0][2] == board[1][2] == board[2][2] == 'X',
              board[0][0] == board[0][1] == board[0][2] == 'X',
              board[1][0] == board[1][1] == board[1][2] == 'X',
              board[2][0] == board[2][1] == board[2][2] == 'X',
              board[0][0] == board[1][1] == board[2][2] == 'X',
              board[2][0] == board[1][1] == board[0][2] == 'X']

    o_wins = [board[0][0] == board[1][0] == board[2][0] == 'O',
              board[0][1] == board[1][1] == board[2][1] == 'O',
              board[0][2] == board[1][2] == board[2][2] == 'O',
              board[0][0] == board[0][1] == board[0][2] == 'O',
              board[1][0] == board[1][1] == board[1][2] == 'O',
              board[2][0] == board[2][1] == board[2][2] == 'O',
              board[0][0] == board[1][1] == board[2][2] == 'O',
              board[2][0] == board[1][1] == board[0][2] == 'O']

    if any(x_wins):
        winner = 'X'
        win = True
    if any(o_wins):
        winner = 'O'
        win = True
    if is_board_full():
        winner = 'D'
        win = True


def is_board_full():
    global board
    count = 0
    for i in range(3):
        for j in range(3):
            if board[j][i] == 'X' or board[j][i] == 'O':
                count += 1

    if count == 9:
        return True


while run:

    CLOCK.tick(FPS)  # setting refreshing rate of display

    SCREEN.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    handle_key_events()

    if not playing:
        if displaying_help_menu:
            help_menu()
        else:
            menu()
    else:
        if flag:
            time.sleep(2)
            resetGame()

        draw()

        if win:
            time.sleep(1)
            SCREEN.fill(WHITE)

        if winner == 'X':
            renderText(winner + " won!", 60, PLAYER_1)
            flag = True
        elif winner == 'O':
            renderText(winner + " won!", 60, PLAYER_0)
            flag = True
        elif winner == 'D':
            renderText("Tie!", 60, BLUE)
            flag = True

        check_win()

    pygame.display.flip()


pygame.quit()
sys.exit()
