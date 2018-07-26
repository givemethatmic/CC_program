# coding=utf-8

import pygame
from CC_board_config import ChessBoard
import CC_chessman_config as Chess
from sys import exit
import socket
from threading import Thread

def change_pos():
    for element2 in range(9):
            for element3 in range(10):
                try:
                    name2 = ChessBoard.board[element2][element3].name
                    color2 = ChessBoard.board[element2][element3].colorRGB
                    pos_x2, pos_y2 = ChessBoard.chess_pos[element2, element3]
                    screen.blit(my_font.render(name2, True, color2), (pos_x2 - 10, pos_y2 - 10))
                except AttributeError:
                    pass


def show_pos():
    while True:
        exec(c.recv(1024).decode())
        global previous_chess_color
        previous_chess_color = 'green'
        screen.fill([255, 255, 255])
        screen.blit(board_image, (0, 0))
        change_pos()
        pygame.display.update()


s = socket.socket()
host = socket.gethostbyname(socket.gethostname())
port = 12345
s.bind((host, port))

mouse_y = -1
mouse_x = -1
BeingSelect = 0
RedKey_x = 4
RedKey_y = 0
GreenKey_x = 4
GreenKey_y = 9
previous_chess_color = 'green'

pygame.init()
ChessBoard.init()

board_image = pygame.image.load("board.png")
pygame.display.set_caption('中国象棋')
screen = pygame.display.set_mode([640, 480])
my_font = pygame.font.Font("/Library/Fonts/BigCaslon.ttf", 20)
font_height = my_font.get_linesize()
for a in dir(Chess):
    try:
        ChessBoard.board[getattr(Chess, a).pos_x][getattr(Chess, a).pos_y] = getattr(Chess, a)
    except AttributeError:
        pass
s.listen(5)
c, address = s.accept()

thd = Thread(target=show_pos)
thd.daemon = True
thd.start()

while True:
    screen.fill([255, 255, 255])
    screen.blit(board_image, (0, 0))
    change_pos()
    pygame.display.update()
    event = pygame.event.wait()
    if event.type == pygame.QUIT:
        exit()
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x, mouse_y = ChessBoard.change_position(mouse_x, mouse_y)
        pos_x, pos_y = ChessBoard.chess_select[mouse_x, mouse_y]
        try:
            BeingSelect = ChessBoard.board[pos_x][pos_y]
            if BeingSelect.color != previous_chess_color:
                screen.blit(my_font.render(BeingSelect.name, True, (0, 0, 0)), (mouse_x - 10, mouse_y - 10))
                pygame.display.update()
                while True:
                    event = pygame.event.wait()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        mouse_x, mouse_y = ChessBoard.change_position(mouse_x, mouse_y)
                        pos_x_new, pos_y_new = ChessBoard.chess_select[mouse_x, mouse_y]
                        try:
                            NextChessColor = ChessBoard.board[pos_x_new][pos_y_new].color
                        except AttributeError:
                            NextChessColor = 'black'
                        if NextChessColor != BeingSelect.color:
                            if not BeingSelect.move(pos_x_new, pos_y_new, ChessBoard.board):
                                if BeingSelect.name == 'Jag':
                                    RedKey_x = BeingSelect.pos_x
                                    RedKey_y = BeingSelect.pos_y
                                elif BeingSelect.name == 'Sai':
                                    GreenKey_x = BeingSelect.pos_x
                                    GreenKey_y = BeingSelect.pos_y
                                while BeingSelect.pos_x == RedKey_x and BeingSelect.pos_y == RedKey_y:
                                    event = pygame.event.wait()
                                    if event.type == pygame.QUIT:
                                        exit()
                                    screen.blit(my_font.render('The Red Lose', True, (255, 0, 0)), (310, 230))
                                    pygame.display.update()
                                while BeingSelect.pos_x == GreenKey_x and BeingSelect.pos_y == GreenKey_y:
                                    event = pygame.event.wait()
                                    if event.type == pygame.QUIT:
                                        exit()
                                    screen.blit(my_font.render('The Green Lose', True, (0, 255, 0)), (310, 230))
                                    pygame.display.update()
                                ChessBoard.board[pos_x][pos_y] = 0
                                ChessBoard.board[BeingSelect.pos_x][BeingSelect.pos_y] = BeingSelect
                                previous_chess_color = BeingSelect.color
                                previous_data = ('ChessBoard.board[' + str(pos_x) + '][' + str(pos_y) + ']')
                                next_data = ('ChessBoard.board[' + str(BeingSelect.pos_x) + '][' + str(BeingSelect.pos_y) + ']')
                                the_package = (next_data + '=' + previous_data + '\n' + previous_data + '=0')
                                c.send(the_package.encode())
                                BeingSelect = 0
                                break
                        elif ChessBoard.board[pos_x_new][pos_y_new] == BeingSelect:
                            break
        except AttributeError:
            pass
