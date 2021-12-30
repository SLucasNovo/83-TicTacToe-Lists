
##### Tic Tac Toe Project

import pandas as pd


players = ['X', 'O']


# Printing board so that is appealing
def print_board(current_board):
    for k, j in enumerate(current_board):
        if k < 2:
            print(f' {j[0]} | {j[1]} | {j[2]} ')
            print(' __________ ')
        else:
            print(f' {j[0]} | {j[1]} | {j[2]} ')


# Creating initial board a grid with 3x3
def refresh_board():
    initial_board = [
        [' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']
    ]
    return initial_board


# 1st check winning diagonals
def check_diagonals(current_board):
    diagonal_1 = []
    diagonal_2 = []
    for p in players:
        for j, k in enumerate(current_board):
            diagonal_1.append(current_board[j][j])
            diagonal_2.append(current_board[-j-1][j])
        if diagonal_1.count(p) == 3 or diagonal_2.count(p) == 3:
            return p


# 2nd check winning columns used pd dataframe here
def check_columns(current_board):
    df_board = pd.DataFrame(current_board)
    for p in players:
        for i in range(3):
            try:
                if df_board[i].value_counts()[p] == 3:
                    return p
            except KeyError:
                pass


# Check if there is a winner
def check_row(current_board):
    for p in players:
        # check row
        for i in current_board:
            if i.count(p) == 3:
                return p


# Checking ir active player has won this function is called after player
def check_winner(current_board):
    row = check_row(current_board)
    column = check_columns(current_board)
    diagonal = check_diagonals(current_board)
    result_list = [row, column, diagonal]
    for result in result_list:
        if result:
            return result


# Translate the letters input to a move in the board
def coordinates_translation(current_board, current_player, move_column: str, move_row: str):
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
    if current_board[row][column] == ' ':
        current_board[row][column] = current_player
        return current_board


# ask the user the move he wants to do
def single_move(current_player, board_state):
    print_board(board_state)
    print(f'Player {current_player} to play:')
    move_column = input('Where do you want to play column-wise? Choose one between l/c/r for left/center/right  \n')
    move_row = input('Where do you want to play row-wise? Choose one between  t/m/b for top/middle/bottom \n')
    get_move = [move_column, move_row]
    return get_move


# check if the move is legal, either it has already been played or it has reached the limit of the board
def legal_move_check(all_moves, current_move):
    if current_move in all_moves or current_move[0] not in ['c', 'l', 'r'] or current_move[1] not in ['t', 'm', 'b']:
        return 1
    if len(current_move) > 8:
        return 2


# Start game
board = refresh_board()
print('Welcome to Tic-Tac-Toe')

moves = []
game = True
while game:
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
