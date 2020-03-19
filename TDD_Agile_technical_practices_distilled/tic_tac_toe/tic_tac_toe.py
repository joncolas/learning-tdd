import sys


class PositionAlreadyPlayed(Exception):
    pass


def set_position(turn, board):
    position = int(input('Player {} turn,'
                         ' please insert position'.format(turn)))
    if board[position] == " ":
        board[position] = turn
    else:
        raise PositionAlreadyPlayed('Position already played,'
                                    ' please use another position')


def check_score(turn, board):
    if board[1] == board[2] == board[3] != ' ' or \
            board[1] == board[4] == board[7] != ' ' or \
            board[1] == board[5] == board[9] != ' ' or \
            board[2] == board[5] == board[8] != ' ' or \
            board[3] == board[6] == board[9] != ' ' or \
            board[7] == board[8] == board[9] != ' ' or \
            board[4] == board[5] == board[6] != ' ' or \
            board[3] == board[5] == board[7] != ' ':
        print("Game Over.\n**** Player {} wins ****".format(turn))
        show_game_board(board)
        sys.exit()


def show_game_board(board):
    print("GAME BOARD")
    print(" {}|{}|{}".format(board[1], board[2], board[3]))
    print("--+-+--")
    print(" {}|{}|{}".format(board[4], board[5], board[6]))
    print("--+-+--")
    print(" {}|{}|{}".format(board[7], board[8], board[9]))


def main():
    board = {
        1: " ", 2: " ", 3: " ",
        4: " ", 5: " ", 6: " ",
        7: " ", 8: " ", 9: " "
    }
    turn = 'X'
    # 9 turns
    for i in range(9):
        show_game_board(board)
        set_position(turn, board)
        check_score(turn, board)
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'
    show_game_board(board)
    print("DRAW")


if __name__ == '__main__':
    main()
