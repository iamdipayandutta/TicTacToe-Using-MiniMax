# Understanding the MiniMax Algorithm

## What is MiniMax?
MiniMax is a decision-making algorithm used in two-player games to find the optimal move. It works by simulating all possible game states and choosing the move that minimizes the maximum possible loss.

## How MiniMax Works in Tic Tac Toe

### Basic Concepts
1. **Maximizer**: The AI player (O) trying to get the highest score
2. **Minimizer**: The human player (X) trying to get the lowest score
3. **Scoring**:
   - Win for AI (O) = +1
   - Win for Human (X) = -1
   - Draw = 0

### Algorithm Steps
1. **Generate Game Tree**
   - Start with current board state
   - Generate all possible moves
   - For each move, create child nodes
   - Continue until reaching terminal states (win/draw)

2. **Evaluate Positions**
   ```
   function minimax(board, depth, isMaximizing):
       if game is over:
           return score
           
       if isMaximizing:
           bestScore = -∞
           for each possible move:
               make move
               score = minimax(board, depth+1, false)
               undo move
               bestScore = max(score, bestScore)
           return bestScore
           
       else:
           bestScore = +∞
           for each possible move:
               make move
               score = minimax(board, depth+1, true)
               undo move
               bestScore = min(score, bestScore)
           return bestScore
   ```

### Example Game Tree
```
                    Root (Max)
                    /    |    \
                   /     |     \
              Min       Min    Min
             /|\       /|\    /|\
           ...  ...  ...  ... ... ...
```

## Implementation Details

### Scoring System
```python
scores = {
    "X": -1,  # Human wins
    "O": +1,  # AI wins
    "tie": 0  # Draw
}
```

### Key Functions
1. **find_best_move**: Entry point for AI decision
2. **minimax**: Recursive function evaluating positions
3. **check_winner**: Evaluates if current state is terminal

## Time Complexity
- Worst case: O(b^d)
  - b = branching factor (available moves)
  - d = maximum depth of tree
- For Tic Tac Toe: approximately 9! = 362,880 positions

## Optimization Possibilities
1. Alpha-Beta Pruning
2. Depth Limited Search
3. Position Caching

## Why MiniMax is Unbeatable in Tic Tac Toe
- Explores complete game tree
- Always chooses optimal move
- Perfect play leads to draw at worst

## Resources for Further Learning
1. Game Theory Basics
2. Tree Traversal Algorithms
3. Advanced AI Game Techniques
