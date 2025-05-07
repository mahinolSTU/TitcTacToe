# TitcTacToe
# Author Name: Md Mahinol Islam
Project for coursework
# Introduction
## Application:
The Tic-Tac-Toe game is a classic two-player game implemented in Python using object-oriented programming (OOP). One player is human, and the other is a computer opponent. Players take turns placing their marks (X or O) on a 3×3 grid. The goal is to align three marks in a row, column, or diagonal. The game ends with a win or a draw.
# Run Program
## Requirements:

Ensure Python 3 is installed.

Download tic_tac_toe.py and test_game.py files to your machine.

### Steps to Run:

1. Open a terminal or command prompt.

2. Navigate to the folder containing the files.

3. un the command:
``` py
python tic_tac_toe.py
```
4. The game will launch in the terminal. Use number keys (1–9) to choose your move.

# Use of Program
-Human player selects positions by entering numbers 1–9.
-The computer player responds automatically.
-The game ends when either player wins or when the board is full (draw).
-Game result is saved to a file named game_history.txt.

# Analysis
## Encapsulation
Encapsulation groups related attributes and methods into single classes and hides internal states from outside interference.

### Example:

``` py
class Board:
    def __init__(self):
        self.board = [" "] * 9

    def display(self):
        # Prints the board

    def update(self, position, symbol):
        # Updates a position

    def is_full(self):
        # Checks if full

    def check_winner(self, symbol):
        # Checks for win
```
All board-related logic is encapsulated in the Board class. Other classes cannot directly modify its data without going through its methods.
## Inheritance
Inheritance lets us reuse code from a base class in derived classes.

### Example:
``` py
class Player:
    def make_move(self, board):  # Abstract method
        raise NotImplementedError

class HumanPlayer(Player):
    def make_move(self, board):
        # Gets user input

class ComputerPlayer(Player):
    def make_move(self, board):
        # Chooses random move
```
Both HumanPlayer and ComputerPlayer inherit from Player, allowing reuse of common logic and enforcing a consistent interface.
## Polymorphism
Polymorphism allows the same method (make_move) to behave differently depending on the object calling it.

### Example:
``` py
player1.make_move(board)
player2.make_move(board)
```
Here, make_move behaves differently for a HumanPlayer and a ComputerPlayer, even though the method name is the same. This allows dynamic interaction in the game loop.

## Abstraction
Abstraction hides complex logic behind simple method calls.
### Example:
``` py
self.board.check_winner(self.current_player.symbol)
```
The game doesn't need to know how the win is checked—just that check_winner() tells whether the current player has won.

## Design Patterns
### 1. Factory Pattern
Used to create player objects dynamically based on type.
### Example:
``` py
def player_factory(player_type, name, symbol):
    if player_type == "human":
        return HumanPlayer(name, symbol)
    elif player_type == "computer":
        return ComputerPlayer(name, symbol)
```
This decouples object creation from game logic.

### 2. Strategy Pattern
Used by polymorphism: Human and Computer players follow different "strategies" for moves but use the same method name (make_move).

## File I/O
The game saves completed match data into a text file (game_history.txt), allowing for later viewing or analysis.
### Example:
``` py
with open("game_history.txt", "a") as file:
    file.write("Game finished:\n")
```
## Testing
Unit tests ensure that the logic works correctly:

check_winner() returns True when there’s a win

is_full() returns True for a draw

Implemented using Python’s built-in unittest module in test_game.py.

## GitHub Upload
Version control is handled using Git:

Initialized repo with git init

Committed changes regularly

Pushed to GitHub for public access and collaboration

## Result
### Achievements:

Fully playable terminal-based game

Supports human vs computer

Implements OOP principles and design patterns

Saves game history to file

Simple test cases added

### Challenges:

Designing clean abstraction between game loop and board logic

Implementing and testing win logic

Learning and applying design patterns

Git version control (commit/push structure)

## Conclusion
#### Key Findings:

The game successfully applied all 4 OOP pillars: Encapsulation, Inheritance, Polymorphism, and Abstraction.

Factory and Strategy patterns allowed clean, scalable design.

Testing and file I/O enhanced the project’s robustness and usability.

#### Achievements:

Clean, modular code

Easy to extend in the future (GUI, multiplayer)

GitHub-ready with testing support

#### Future Prospects:

Add GUI using tkinter or pygame

Add difficulty levels to computer player

Implement multiplayer over network

Add scoreboard or online leaderboard


