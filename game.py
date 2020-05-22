"""Simulation of the game Tic-tac-toe"""
from board import Board, TextException


def check_winner(board):
    """
    (Board) -> bool
    Checks whether the winner is or the game ended
    """
    if board.is_winner()[0]:
        winner = "Computer"
        if board.is_winner()[1] == 5:
            winner = "You"
        print("{} won!".format(winner))
    elif board.is_winner()[1] == "end":
        print("No one won")
    else:
        return True
    return False


def check_user_input(text):
    """
    (str) -> str, str
    Returns positions where person will move
    if user's input is correct. False otherwise.
    """
    try:
        text = text.split(",")
        return text[0], text[1]
    except (TypeError, IndexError):
        print("Invalid input. Must be: 0,0")
        raise TextException


def process(board):
    """
    (Board) ->
    Represents main process of the game
    """
    if not check_winner(board):
        return "stop"
    user_input = input("Print stop to exit. Your turn! Write position to move (in format 0,0): ")
    if user_input == "stop":
        return "stop"
    try:
        pos1, pos2 = check_user_input(user_input)
    except (ValueError, TypeError):
        raise TextException("Invalid input. Must be: 0,0")

    board.person_move(int(pos1), int(pos2))
    print("Board:")
    print(board)

    if not check_winner(board):
        return "stop"
    print("Computer moved:")
    board.computer_move()
    print("Board:")
    print(board)
    return None


def play_game():
    """
    () ->
    Simulation of the game Tic-tac-toe
    """
    board = Board()
    print("Board:")
    print(board)

    counter = True
    while counter:
        try:
            if process(board) == "stop":
                counter = False
        except TextException:
            pass


if __name__ == '__main__':
    play_game()
