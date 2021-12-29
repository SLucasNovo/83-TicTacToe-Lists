
##### Tic Tac Toe Project

import pandas as pd

# TODO1 : Be able to input characters
# todo2: Create Players
# todo3 : check if row winners

players = ['X', 'O']


def print_board(board):
    for k, j in enumerate(board):
        if k < 2:
            print(f' {j[0]} | {j[1]} | {j[2]} ')
            print(' __________ ')
        else:
            print(f' {j[0]} | {j[1]} | {j[2]} ')


def refresh_board():
    initial_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return initial_board


def check_diagonals(board):
    players = ['X', 'O']
    diagonal_1 = []
    diagonal_2 = []
    for player in players:
        for j, k in enumerate(board):
            diagonal_1.append(board[j][j])
            diagonal_2.append(board[-j-1][j])
        if diagonal_1.count(player) == 3 or diagonal_2.count(player) == 3:
            return player


def check_columns(board):
    df_board = pd.DataFrame(board)
    for player in players:
        for i in range(3):
            try:
                if df_board[i].value_counts()[player] == 3:
                    return player
            except KeyError:
                pass

# Check if there is a winner
def check_row(board):
    for player in players:
        # check row
        for i in board:
            if i.count(player) == 3:
                return player
        # check columns


def check_winner(board):
    r = check_row(board)
    c = check_columns(board)
    d = check_diagonals(board)
    result_list = [r, c, d]
    for r in result_list:
        if r:
            return r


#
def coordinates_translation(board, player, move_column: str, move_row: str):

    if move_column.lower() in ['c', 'center']:
        column = 1
    elif move_column.lower() in ['r', 'right']:
        column = 2
    elif move_column.lower() in ['l', 'left']:
        column = 0
    else:
        return False
    if move_row.lower() in ['m', 'middle']:
        row = 1
    elif move_row.lower() in ['b', 'bottom']:
        row = 2
    elif move_row.lower() in ['t', 'top']:
        row = 0
    else:
        return False
    if board[row][column] == ' ':
        board[row][column] = player
        return board

# moves should be :
# Columns: Left Center Right
# Row: Top Middle Bottom


def single_move(player, board_state):
    print_board(board_state)
    print(f'Player {player} to play:')
    move_column = input('Where do you want to play column-wise? Choose one between l/c/r for left/center/right  \n')
    move_row = input('Where do you want to play row-wise? Choose one between  t/m/b for top/middle/bottom \n')
    moves = [move_column, move_row]
    return moves

    # new_board = coordinates_translation(board, player_1, move_column, move_row)
    # print_board(new_board)
    # print(f'Player {player_2} to play:')
    # move_column = input('Where do you want to play column-wise? Choose one between l/c/r for left/center/right  \n')
    # move_row = input('Where do you want to play row-wise? Choose one between  t/m/b for top/middle/bottom \n')
    # new_board = coordinates_translation(board, player_2, move_column, move_row)
    # print_board(new_board)


def legal_move_check(moves, move):
    if move in moves:
        return 1
    if len(move) > 8:
        return 2

board = refresh_board()
print('Welcome to Tic-Tac-Toe')

moves = []
game = True
while game:
    # print_board(board)
    for player in players:
        move = single_move(player, board)
        if legal_move_check(moves, move) == 1:
            print('Choose a valid move.')
            move = single_move(player, board)
        if legal_move_check(moves, move) == 2:
            print('Its a tie.')
            cont = input('Do you want to play again? y/n\n')
            if cont == 'y':
                board = refresh_board()
                moves = []
                break
            elif cont == 'n':
                game = False
                break
        moves.append(move)

        board = coordinates_translation(board, player, move[0], move[1])
        if check_winner(board):
            r = check_winner(board)
            print(f'Player {r} is the winner')
            cont = input('Do you want to play again? y/n\n')
            if cont == 'y':
                board = refresh_board()
                moves = []
                break
            elif cont == 'n':
                game = False

