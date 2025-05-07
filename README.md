# TitcTacToe
# Author Name: Md Mahinol Islam
Project for coursework
# Introduction
## Application:
The Tic-Tac-Toe game is a classic two-player game implemented in Python using object-oriented programming (OOP). One player is human, and the other is a computer opponent. Players take turns placing their marks (X or O) on a 3×3 grid. The goal is to align three marks in a row, column, or diagonal. The game ends with a win or a draw.
# Run Program


1. Ensure Python 3 is installed.
2. Download the tic_tac_toe.py file.
3. Open a terminal or command prompt.
4. Navigate to the file directory.
5. Run the command: python `tic_tac_toe.py`.


## Requirements:

Ensure Python 3 is installed.

Download `tic_tac_toe.py` and test_game.py files to your machine.

### Steps to Run:

1. Open a terminal or command prompt.

2. Navigate to the folder containing the files.

3. un the command:
``` py
python tic_tac_toe.py
```
4. The game will launch in the terminal. Use number keys (1–9) to choose your move.

# Use of Program
1. Human player selects positions by entering numbers 1–9.
2. The computer player responds automatically.
3. The game ends when either player wins or when the board is full (draw).
4. Game result is saved to a file named game_history.txt.

# Analysis
The Tic-Tac-Toe game demonstrates OOP principles and design patterns in Python. It includes:
1. Encapsulation
2. Inheritance
3. Polymorphism
4. Abstraction
5. Factory and Strategy Design Patterns
## Encapsulation
Encapsulation is one of the four main pillars of Object-Oriented Programming (OOP). It means:
Bundling data (variables) and the methods (functions) that work on that data into a single unit (a class), and controlling access to that data.
In simple words:
Internal details are kept private or protected inside a class.
Other parts of the program interact through methods, not by changing variables directly.

### Example:

``` py
class Board:
    def __init__(self):
        self.board = [" "] * 9

    def update(self, position, symbol):
        self.board[position] = symbol

    def display(self):
        # prints the board layout

    def is_full(self):
        return " " not in self.board
        # Checks for win
```
The `Board` class manages board data privately. Other classes access it only through methods like `update()`, `is_full()`, `or display()`.
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
Both `HumanPlayer` and `ComputerPlayer` inherit from `Player`, allowing reuse of common logic and enforcing a consistent interface. override the abstract `make_move()` method.
## Polymorphism
Polymorphism allows the same method (make_move) to behave differently depending on the object calling it.

### Example:
``` py
def play(self):
    position = self.current_player.make_move(self.board.board)
#or
player1.make_move(board)
player2.make_move(board)
```
1. If `current_player` is a `HumanPlayer`, it takes user input.
2. If it is a `ComputerPlayer`, it chooses a random empty spot.
Same method name, different behavior.

## Abstraction
Abstract refers to hiding the complex internal logic and exposing only the necessary interface.
In Python, an abstract class is like a blueprint that other classes must follow. It cannot be used directly — only its child classes can use it by completing its structure.


### Example:
``` py
self.board.check_winner(self.current_player.symbol)
```
The game doesn't need to know how the win is checked—just that `check_winner()` tells whether the current player has won.

## Design Patterns
### 1. Factory Pattern
The factory pattern is used to create objects without specifying their exact class.
### Example:
``` py
def player_factory(player_type, name, symbol):
    if player_type == "human":
        return HumanPlayer(name, symbol)
    elif player_type == "computer":
        return ComputerPlayer(name, symbol)
```
Depending on `player_type`, it creates and returns the appropriate player class.

### 2. Strategy Pattern
Used by polymorphism: Human and Computer players follow different "strategies" for moves but use the same method name (make_move).

``` py
lass HumanPlayer(Player):
    def make_move(self, board):
        # takes user input

class ComputerPlayer(Player):
    def make_move(self, board):
        # selects random move
```
Both use the `make_move()` method but follow different strategies.



# Result

### Achievements:

1. Successfully implemented a turn-based game with AI.
2. Clean code using OOP design.
3. Game results saved to file.

### Challenges:

1. Managing game state and win-check logic.
2. Ensuring proper separation between game logic and UI.
3. Handling input validation.

### Game Logic:

1. Each move is validated.
2. Win condition checked after every move.
3. Draw detected if board is full.
4. Final board written to `game_history.txt`.

## Conclusion
#### Key Findings:

1. The game successfully applied all 4 OOP pillars: Encapsulation, Inheritance, Polymorphism, and Abstraction.
2. Factory and Strategy patterns allowed clean, scalable design.
3. Testing and file I/O enhanced the project’s robustness and usability.

#### Achievements:

1. Clean, modular code
2. Easy to extend in the future (GUI, multiplayer)
3. GitHub-ready with testing support

#### Future Prospects:

1. Add GUI using tkinter or pygame
2. Add difficulty levels to computer player
3. Implement multiplayer over network
4. Add scoreboard or online leaderboard


