import random


class GameBoard:
    def __init__(self):
        self.board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]

    def draw_board(self):
        for row in self.board:
            print(" | ".join(row))

    def check_spot_empty(self, row, col):
        if self.board[row][col] == " ":
            return True
        else:
            return False

    def player_move(self):
        print("Player 1's turn")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if self.check_spot_empty(row, col):
            self.board[row][col] = "X"
        else:
            print("Spot is already taken")
            self.player_move()

    def computer_move(self):
        print("Computer's turn")
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.check_spot_empty(row, col):
            self.board[row][col] = "O"
        else:
            self.computer_move()

    def check_for_winner(self):
        # horizontal check
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return True

        # vertical check
        for i in range(3):
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != " ":
                return True

        # diagonal check
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return True

        return False

    def play(self):
        while True:
            self.draw_board()
            self.player_move()
            if self.check_for_winner():
                self.draw_board()
                print("Player 1 wins!")
                break
            self.draw_board()
            self.computer_move()
            if self.check_for_winner():
                self.draw_board()
                print("Computer wins!")
                break


if __name__ == "__main__":
    game_board = GameBoard()
    game_board.play()