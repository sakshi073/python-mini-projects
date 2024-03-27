import math
import random
import time

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Representing the 3x3 Tic-Tac-Toe board
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        # Check row
        row_ind = square // 3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot == letter for spot in row]):
            return True
        # Check column
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        # Check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        return False

class HumanPlayer:
    def __init__(self, letter, name):
        self.letter = letter
        self.name = name

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            try:
                square = int(input(f"{self.name}'s turn ({self.letter}). Enter a number (0-8): "))
                if square not in range(9):
                    raise ValueError
                if square not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid input. Please enter a valid number (0-8) for an empty spot.')

        return square

def play_tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")

    player1_name = input("Enter Player 1's name: ")
    player2_name = input("Enter Player 2's name: ")

    player1 = HumanPlayer('X', player1_name)
    player2 = HumanPlayer('O', player2_name)

    while True:
        t = TicTacToe()
        current_player = player1

        while t.empty_squares():
            t.print_board()
            square = current_player.get_move(t)
            t.make_move(square, current_player.letter)

            if t.current_winner:
                t.print_board()
                print(f"{current_player.name} wins!")
                break

            current_player = player2 if current_player == player1 else player1

        if not t.current_winner:
            t.print_board()
            print("It's a tie!")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

if __name__ == '__main__':
    play_tic_tac_toe()
