"""Represents a Board"""
import random
import copy
from btree import LinkedBinaryTree


class TextException(Exception):
    """Exception for invalid inputs in the game"""


class Board:
    """Represents a Board"""
    def __init__(self):
        """
        () ->
        Initialize a board
        """
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.last_move = None

    def __str__(self):
        """
        () -> str
        Returns string that represents a board
        """
        result = ""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 5:
                    result += " x"
                elif self.board[i][j] == 7:
                    result += " о"
                else:
                    result += " #"
            result += "\n"
        return result

    def available_combinations(self):
        """
        () -> list
        Returns available combinations to move
        """
        result = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    result.append((i, j))

        return result

    def person_move(self, pos1=None, pos2=None):
        """
        (int, int) ->
        Users moving in the game
        """
        if self.available_combinations() != []:
            if pos1 is None and pos2 is None:
                comb = random.choice(self.available_combinations())
                self.board[comb[0]][comb[1]] = 5
            else:
                if (pos1, pos2) in self.available_combinations():
                    self.board[pos1][pos2] = 5
                else:
                    print("This position is not available")
                    raise TextException
            self.last_move = 5

    def create_tree(self, tree):
        """
        (LinkedBinaryTree) ->
        Recursion method to create a tree fot the game
        """
        # print(self)
        if len(self.available_combinations()) > 1:
            comb1 = random.choice(self.available_combinations())
            comb2 = random.choice(self.available_combinations())

            if self.last_move == 5:
                next_move = 7
            else:
                next_move = 5

            # print(next_move)

            board1 = copy.deepcopy(self)
            board2 = copy.deepcopy(self)

            board1.board[comb1[0]][comb1[1]] = next_move
            board1.last_move = 7
            tree.insert_left(board1)
            board2.board[comb2[0]][comb2[1]] = next_move
            board2.last_move = 7
            tree.insert_right(board2)

            board1.create_tree(tree.get_left_child())
            board2.create_tree(tree.get_left_child())

    @staticmethod
    def _calculate_points(tree):
        """
        (LinkedBinaryTree) ->
        Calculates points for one of the tree's side
        to choose better position to move
        """
        leafs = []
        points = 0

        def order(tree):
            if tree is not None:
                if tree.get_left_child() is not None:
                    order(tree.get_left_child())
                elif tree.get_right_child() is not None:
                    order(tree.get_right_child())
                else:
                    leafs.append(tree.key)

        order(tree)

        for board in leafs:
            if board.is_winner()[0]:
                if board.is_winner()[1] == 5:
                    points -= 1
                else:
                    points += 1

        return points

    def computer_move(self):
        """
        () ->
        Computer moving in the game
        """
        tree = LinkedBinaryTree(self)
        self.create_tree(tree)
        left_points = self._calculate_points(tree.get_left_child())
        right_points = self._calculate_points(tree.get_right_child())

        if left_points < right_points:
            next_board = tree.get_right_child().key
        else:
            next_board = tree.get_left_child().key
        self.board = next_board.board

    def is_winner(self):
        """
        () -> bool, str
        Returns True if one of the players won,
        and False otherwise
        """
        for i in range(3):
            if (self.board[i][0] == self.board[i][1] == self.board[i][2]) \
                    and (self.board[i][0] != 0):
                return True, self.board[i][0]

            if self.board[0][i] == self.board[1][i] == self.board[2][i] \
                    and (self.board[0][i] != 0):
                return True, self.board[0][i]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] \
                and (self.board[0][0] != 0):
            return True, self.board[0][0]

        if self.board[2][0] == self.board[1][1] == self.board[0][2] \
                and (self.board[2][0] != 0):
            return True, self.board[2][0]

        if self.available_combinations() == []:
            return False, 'end'

        return False, None
