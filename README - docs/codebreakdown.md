# Code Breakdown: Tic Tac Toe Using MiniMax

This document provides a step-by-step explanation of how to build a Tic Tac Toe game with an unbeatable AI using the MiniMax algorithm. This guide is designed for beginners!

---

## 1. Game Board Representation 🎮
We represent the game board as a 3x3 grid using a 2D list. Think of it like this:
```
 0,0 | 0,1 | 0,2
-----|-----|-----
 1,0 | 1,1 | 1,2
-----|-----|-----
 2,0 | 2,1 | 2,2
```

Each cell can contain:
- 'X' (Player)
- 'O' (Computer)
- ' ' (Empty space)

### Example Board Code:
```python
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]
```

## 2. MiniMax Algorithm 🤖
Think of MiniMax as the computer thinking ahead like a chess player:
1. It looks at all possible moves
2. For each move, it thinks: "If I do this, what could happen?"
3. It keeps going until it finds a win/loss/draw
4. It picks the move that gives the best outcome

### How MiniMax Thinks:
```
Score values:
+10 = AI wins
-10 = Player wins
 0  = Draw

      [Root]
    /    |    \
   /     |     \
[+10]  [0]    [-10]
```

### Example Code:
```python
# filepath: minimax.py
def minimax(board, depth, is_maximizing):
    if check_winner(board) == 'X':
        return 10 - depth
    elif check_winner(board) == 'O':
        return depth - 10
    elif is_draw(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for move in get_available_moves(board):
            make_move(board, move, 'X')
            score = minimax(board, depth + 1, False)
            undo_move(board, move)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for move in get_available_moves(board):
            make_move(board, move, 'O')
            score = minimax(board, depth + 1, True)
            undo_move(board, move)
            best_score = min(best_score, score)
        return best_score
```

## 3. Understanding the Code Flow 🔄

Here's how the game runs step by step:
1. Display empty board
2. Player makes move (choosing coordinates)
3. AI analyzes board using MiniMax
4. AI makes the best possible move
5. Repeat until game ends

### Implementation Tips for Beginners:
- Start by implementing the basic board display
- Add move validation next
- Implement win checking
- Finally, add the AI with MiniMax

## 4. Testing Your Game 🎯
Test these scenarios:
1. Can player make valid moves?
2. Does the program detect wins correctly?
3. Can the AI block winning moves?
4. Is the AI unbeatable?

## 5. Common Beginner Mistakes to Avoid ⚠️
1. Not validating player moves
2. Forgetting to check for draws
3. Not handling invalid input
4. Recursive depth issues in MiniMax

## 7. Backend Folder Structure 📁

The `backend/` folder contains these Python files:

### app.py
Flask server that handles the game API:
```python
# Key functions:
- make_move(): Handles POST /move for player moves
- reset_game(): Handles POST /reset
- get_state(): Handles GET /state
```

### main.py
Game controller:
```python
# Key functions:
- init_board(): Creates new game board
- make_move(): Places a move on the board
- main(): Runs the game loop
```

### game_logic.py
Core game rules:
```python
# Key functions:
- check_winner(): Checks for winning combinations
- is_draw(): Checks for draw condition
- game_over(): Checks if game has ended
```

### minimax.py
AI implementation:
```python
# Key functions:
- get_best_move(): Finds optimal AI move
- minimax(): Implements minimax algorithm
- get_available_moves(): Gets possible moves
```

### ui.py
Console interface:
```python
# Key functions:
- print_board(): Displays game state
- get_player_move(): Gets player input
```

## File Dependencies:
```
app.py (Flask API)
  └── minimax.py
main.py
  ├── game_logic.py
  ├── minimax.py
  └── ui.py
```



