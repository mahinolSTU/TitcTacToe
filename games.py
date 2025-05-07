
import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        raise NotImplementedError("This method must be overridden.")


class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                position = int(input(f"{self.name} ({self.symbol}), choose (1-9): ")) - 1
                if position not in range(9):
                    print("Choose a number from 1 to 9.")
                elif board[position] != " ":
                    print("Spot already taken.")
                else:
                    return position
            except ValueError:
                print("Enter a valid number.")


class ComputerPlayer(Player):
    def make_move(self, board):
        available = [i for i, x in enumerate(board) if x == " "]
        return random.choice(available)


class Board:
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        print("\n")
        for i in range(3):
            print(f" {self.board[i*3]} | {self.board[i*3+1]} | {self.board[i*3+2]} ")
            if i < 2:
                print("---+---+---")
        print("\n")

    def update(self, position, symbol):
        self.board[position] = symbol

    def is_full(self):
        return " " not in self.board

    def check_winner(self, symbol):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.board[i] == symbol for i in line) for line in wins)


def player_factory(player_type, name, symbol):
    if player_type == "human":
        return HumanPlayer(name, symbol)
    elif player_type == "computer":
        return ComputerPlayer(name, symbol)


class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.current_player = player1
        self.other_player = player2
        self.log_file = "game_history.txt"

    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def save_game(self):
        with open(self.log_file, "a") as file:
            file.write("Game finished:\n")
            for i in range(3):
                row = self.board.board[i * 3:(i + 1) * 3]
                file.write(" | ".join(row) + "\n")
            file.write("\n")

    def play(self):
        print("🎮 Tic-Tac-Toe Game Starts!")
        self.board.display()

        while True:
            pos = self.current_player.make_move(self.board.board)
            self.board.update(pos, self.current_player.symbol)
            self.board.display()

            if self.board.check_winner(self.current_player.symbol):
                print(f"{self.current_player.name} ({self.current_player.symbol}) wins!")
                self.save_game()
                break
            elif self.board.is_full():
                print("It's a draw!")
                self.save_game()
                break

            self.switch_players()

        print("Game over!")

if __name__ == "__main__":
    print("Choose players:")
    player1 = player_factory("human", "Player 1", "X")
    player2 = player_factory("computer", "Computer", "O")
    game = Game(player1, player2)
    game.play()
