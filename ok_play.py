import numpy as np
import pygame
import sys

WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
YELLOW = (255,255,0)
BLACK = (0,0,0)

TILE_NUMBER = 15

ROW_COUNT = 20
COLUMN_COUNT = 20

def contiguous(board):
    visited_array = []
    for row in range(ROW_COUNT+1):
        row = []
        for col in range(COLUMN_COUNT+1):
            row.append("X")
        visited_array.append(row)
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if board[row][col] != 0.:
                visited_array[row+1][col+1] = "U"
    # for row in visited_array:
    #     print(row)

    def can_visit(visited_array, row, col): # This is the recursive function, it returns true when it finds the path and traces it
        if visited_array[row][col] == "U":
            visited_array[row][col] = "V"
        elif visited_array[row][col] == "V" or visited_array[row][col] == "X":
            return False
        directions = [(row, col+1), (row, col-1), (row+1, col), (row-1, col)]
        for direction in directions:
            x = can_visit(visited_array, direction[0], direction[1])
            if x:
                return True
        return False
    can_visit_ran = False

    for row in range(1,ROW_COUNT):
        for col in range(1,COLUMN_COUNT):
            if visited_array[row][col] == "U":
                can_visit(visited_array, row, col)
                can_visit_ran = True
                break
        if can_visit_ran is True:
            break

    # for row in visited_array:
    #     print(row)
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            if visited_array[row][col] == "U":
                return False
    return True



def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    board[ROW_COUNT//2][COLUMN_COUNT//2] = 1
    return board


def is_valid_location(board, row, col):
    if board[row][col] == 0:
        if board[row + 1][col] != 0.:
            return True
        elif board[row - 1][col] != 0.:
            return True
        elif board[row][col + 1] != 0.:
            return True
        elif board[row][col - 1] != 0.:
            return True
        else:
            return False
    else:
        return False


def is_good(board):
    if contiguous(board):
        return True
    # for col in range(1, COLUMN_COUNT-1):
    #     for row in range(1, ROW_COUNT-1):
    #         if board[row][col] != 0:
    #             if board[row+1][col] == 0 and board[row-1][col] == 0 and board[row][col+1] == 0 and board[row][col-1] == 0:
    #                 return False
                # if board[row+1][col+1] != 0.:
                #     if board[row+1][col] == 0. and board[row][col+1] == 0.:
                #         print(f"{row}, {col}")
                #         print("fail1")
                #         return False
                # elif board[row+1][col-1] != 0.:
                #     if board[row+1][col] == 0. and board[row][col-1] == 0.:
                #         print("fail2")
                #         return False
                # elif board[row-1][col+1] != 0.:
                #     if board[row - 1][col] == 0. and board[row][col + 1] == 0.:
                #         print("fail3")
                #         return False
                # elif board[row-1][col-1] != 0.:
                #     if board[row - 1][col] == 0. and board[row][col - 1] == 0.:
                #         print("fail4")
                #         return False
    # if search_zeroes(board):
    #     print("two islands")
    #     return False
    # return True

# def search_one_tile_south(board, row):
#     tile_count = 0
#     for col in board[row+1]:
#         if col != 0:
#             tile_count += 1
#     if tile_count == 1:
#         return True
#
# def search_one_tile_north(board, row):
#     tile_count = 0
#     for col in board[row - 1]:
#         if col != 0:
#             tile_count += 1
#     if tile_count == 1:
#         return True
                # tile_count2 = 0
                # for col in board[roww-1]:
                #     if col != 0:
                #         tile_count2 += 1
                # if tile_count2 == 1:
                #     return True
                # tile_count3 = 0
                # for row in board:
                #     if row[coll+1] != 0:
                #         tile_count3 += 1
                # if tile_count3 == 1:
                #     return True
                # tile_count4 = 0
                # for row in board:
                #     if row[coll-1] != 0:
                #         tile_count4 += 1
                # if tile_count4 == 1:
                #     return True




def search_zeroes(board):
    for roww in range(2, COLUMN_COUNT-2):
        for coll in range(2, ROW_COUNT-2):
            if board[roww][coll] != 0.:
                if board[roww+2][coll] != 0.:
                    all_0 = True
                    for col in board[roww+1]:
                        if col != 0:
                            all_0 = False
                    if all_0:
                        return True
                elif board[roww-2][coll] != 0.:
                    all_0 = True
                    for col in board[roww - 1]:
                        if col != 0:
                            all_0 = False
                    if all_0:
                        return True
                elif board[roww][coll+2] != 0.:
                    all_0 = True
                    for row in board:
                        if row[coll+1] != 0:
                            all_0 = False
                    if all_0:
                        return True
                elif board[roww][coll-2] != 0.:
                    all_0 = True
                    for row in board:
                        if row[coll - 1] != 0:
                            all_0 = False
                    if all_0:
                        return True
    return False




def drop_piece(board, row, col, piece):
        board[row][col] = piece


def print_board(board):
    # print(np.flip(board, 0))
    print(board)

def winning_move(board, piece):
    # check for horizontal locations for win
    for c in range(COLUMN_COUNT - 4):
        for r in range(ROW_COUNT):
            if board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][c + 3] == piece and board[r][c+4] == piece:
                return True

    # check vertical locations for win
    for c in range(COLUMN_COUNT):
        for r in range(ROW_COUNT - 4):
            if board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] == piece and board[r + 3][c] == piece and board[r+4][c] == piece:
                return True

    # Check positively sloped diaganols
    for c in range(COLUMN_COUNT - 4):
        for r in range(ROW_COUNT - 4):
            if board[r][c] == piece and board[r + 1][c + 1] == piece and board[r + 2][c + 2] == piece and board[r + 3][c + 3] == piece and board[r+4][c+4] == piece:
                return True

    # Check negatively sloped diaganols
    for c in range(COLUMN_COUNT - 4):
        for r in range(4, ROW_COUNT):
            if board[r][c] == piece and board[r - 1][c + 1] == piece and board[r - 2][c + 2] == piece and board[r - 3][c + 3] == piece and board[r-4][c+4] == piece:
                return True



def draw_board(board):
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            pygame.draw.rect(screen, BLACK, (col*SQUARESIZE, row*SQUARESIZE, SQUARESIZE, SQUARESIZE))
            pygame.draw.rect(screen, WHITE, ((col*SQUARESIZE)+1, (row*SQUARESIZE)+1, SQUARESIZE-2, SQUARESIZE-2))
    for col in range(COLUMN_COUNT):
        for row in range(ROW_COUNT):
            if board[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col*SQUARESIZE+1, row*SQUARESIZE+1, SQUARESIZE - 2, SQUARESIZE - 2))
            elif board[row][col] == 2:
                pygame.draw.rect(screen, RED, (col*SQUARESIZE+1, row*SQUARESIZE+1, SQUARESIZE - 2, SQUARESIZE - 2))
            elif board[row][col] == 3:
                pygame.draw.rect(screen, GREEN, (col*SQUARESIZE+1, row*SQUARESIZE+1, SQUARESIZE - 2, SQUARESIZE - 2))
            elif board[row][col] == 4:
                pygame.draw.rect(screen, YELLOW, (col*SQUARESIZE+1, row*SQUARESIZE+1, SQUARESIZE - 2, SQUARESIZE - 2))
    pygame.display.update()

board = create_board()
print_board(board)
game_over = False
turn = 1
count = 0
motion = 0

pygame.init()

SQUARESIZE = 35

width = COLUMN_COUNT*SQUARESIZE
height = (ROW_COUNT+1)*SQUARESIZE

size = (width, height)

screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

myfont = pygame.font.SysFont("monospace", 30)

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            draw_board(board)
            posx = event.pos[0]
            posy = event.pos[1]
            if turn == 0:
                pygame.draw.rect(screen, BLUE, (posx-SQUARESIZE//2, posy-SQUARESIZE//2, SQUARESIZE-2,SQUARESIZE-2))
            elif turn == 1:
                pygame.draw.rect(screen, RED, (posx-SQUARESIZE//2, posy-SQUARESIZE//2, SQUARESIZE-2,SQUARESIZE-2))
            elif turn == 2:
                pygame.draw.rect(screen, GREEN, (posx-SQUARESIZE//2, posy-SQUARESIZE//2, SQUARESIZE-2,SQUARESIZE-2))
            elif turn == 3:
                pygame.draw.rect(screen, YELLOW, (posx-SQUARESIZE//2, posy-SQUARESIZE//2, SQUARESIZE-2,SQUARESIZE-2))

        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            draw_board(board)
            if turn == 0:
                posx = event.pos[0]
                posy = event.pos[1]
                col = int(posx // SQUARESIZE) # see how to replace math.floor
                row = int(posy // SQUARESIZE)
                if is_valid_location(board, row, col):
                    drop_piece(board, row, col, 1)
                    if winning_move(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, WHITE)
                        screen.blit(label, (0, SQUARESIZE*ROW_COUNT))
                        print("over")
                        game_over = True
                else:
                    turn -= 1

            elif turn == 1:
                posx = event.pos[0]
                posy = event.pos[1]
                col = int(posx // SQUARESIZE)  # see how to replace math.floor
                row = int(posy // SQUARESIZE)
                if is_valid_location(board, row, col):
                    drop_piece(board, row, col, 2)
                    if winning_move(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, WHITE)
                        screen.blit(label, (0,SQUARESIZE*ROW_COUNT))
                        game_over = True
                else:
                    turn -= 1

            elif turn == 2:
                posx = event.pos[0]
                posy = event.pos[1]
                col = int(posx // SQUARESIZE)  # see how to replace math.floor
                row = int(posy // SQUARESIZE)
                if is_valid_location(board, row, col):
                    drop_piece(board, row, col, 3)
                    if winning_move(board, 3):
                        label = myfont.render("Player 3 wins!!", 1, WHITE)
                        screen.blit(label, (0, SQUARESIZE*ROW_COUNT))
                        game_over = True
                else:
                    turn -= 1
            elif turn == 3:
                posx = event.pos[0]
                posy = event.pos[1]
                col = int(posx // SQUARESIZE)  # see how to replace math.floor
                row = int(posy // SQUARESIZE)
                if is_valid_location(board, row, col):
                    drop_piece(board, row, col, 4)
                    if winning_move(board, 4):
                        label = myfont.render("Player 4 wins!!", 1, WHITE)
                        screen.blit(label, (0, SQUARESIZE*ROW_COUNT))
                        game_over = True
                else:
                    turn -= 1
            print_board(board)
            draw_board(board)

            turn += 1
            if turn % 4 == 0:
                count += 1
            turn = turn % 4

            if count >= TILE_NUMBER:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if turn == 0:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        col = int(posx // SQUARESIZE)  # see how to replace math.floor
                        row = int(posy // SQUARESIZE)
                        if board[row][col] == 1:
                            board[row][col] = 0
                            if is_good(board):
                                draw_board(board)
                            else:
                                board[row][col] = 1
                        else:
                            turn = 0

                    elif turn == 1:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        col = int(posx // SQUARESIZE)  # see how to replace math.floor
                        row = int(posy // SQUARESIZE)
                        if board[row][col] == 2:
                            board[row][col] = 0
                            if is_good(board):
                                draw_board(board)
                                # pygame.draw.rect(screen, WHITE, (
                                #     (col * SQUARESIZE) + 1, (row * SQUARESIZE) + 1, SQUARESIZE - 2, SQUARESIZE - 2))
                            else:
                                board[row][col] = 2
                        else:
                            turn = 1

                    elif turn == 2:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        col = int(posx // SQUARESIZE)  # see how to replace math.floor
                        row = int(posy // SQUARESIZE)
                        if board[row][col] == 3:
                            board[row][col] = 0
                            if is_good(board):
                                draw_board(board)
                            else:
                                board[row][col] = 3
                        else:
                            turn = 2

                    elif turn == 3:
                        posx = event.pos[0]
                        posy = event.pos[1]
                        col = int(posx // SQUARESIZE)  # see how to replace math.floor
                        row = int(posy // SQUARESIZE)
                        if board[row][col] == 4:
                            board[row][col] = 0
                            if is_good(board):
                                draw_board(board)
                            else:
                                board[row][col] = 4
                        else:
                            turn = 3
                    print_board(board)

                    draw_board(board)

            if game_over:
                pygame.time.wait(15000)

# while not game_over:
#     if turn == 0:
#         row = int(input("Player 1, pick row:"))
#         col = int(input("Player 1, pick col:"))
#         if is_valid_location(board, row, col):
#             drop_piece(board,row,col,1)
#         else:
#             turn -= 1
#     elif turn == 1:
#         row = int(input("Player 2, pick row:"))
#         col = int(input("Player 2, pick col:"))
#         if is_valid_location(board, row, col):
#             drop_piece(board,row,col,2)
#         else:
#             turn -= 1
#     elif turn == 2:
#         row = int(input("Player 3, pick row:"))
#         col = int(input("Player 3, pick col:"))
#         if is_valid_location(board, row, col):
#             drop_piece(board,row,col,3)
#         else:
#             turn -= 1
#     elif turn == 3:
#         row = int(input("Player 4, pick row:"))
#         col = int(input("Player 4, pick col:"))
#         if is_valid_location(board, row, col):
#             drop_piece(board,row,col,4)
#         else:
#             turn -= 1
#     print_board(board)
#     turn += 1
#     turn = turn % 4
#
#
#
