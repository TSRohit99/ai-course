# MinMax & Alpha-Beta Pruning Implementation 🎮

A comprehensive Python implementation of game-theoretic algorithms for two-player zero-sum games, featuring both MinMax and Alpha-Beta pruning with a complete Tic-Tac-Toe game demonstration.

## 📋 Table of Contents
- [Algorithms Implemented](#algorithms-implemented)
- [How Algorithms Work](#how-algorithms-work)
- [Applications](#applications)
- [Complexity Analysis](#complexity-analysis)
- [Input & Output Examples](#input--output-examples)
- [Usage](#usage)

## 🚀 Algorithms Implemented

- **MinMax Algorithm** 🎯
- **Alpha-Beta Pruning** ✂️
- **Interactive Tic-Tac-Toe Game** 🎮

## 🧠 How Algorithms Work

### 🎯 MinMax Algorithm
A recursive decision-making algorithm for two-player games. Maximizing player seeks highest score while minimizing player seeks lowest score. Explores entire game tree to find optimal moves assuming both players play perfectly.

### ✂️ Alpha-Beta Pruning
An optimization of MinMax that eliminates branches that cannot influence the final decision. Uses alpha (best maximizer score) and beta (best minimizer score) bounds to prune unnecessary subtrees, significantly reducing computation time.

### 🎮 Game Integration
Complete Tic-Tac-Toe implementation demonstrating practical application where AI (X) plays optimally against human player (O) using Alpha-Beta pruning for move selection.

## 🎯 Applications

### 🎯 MinMax Applications
- **Board Games** - Chess, Checkers, Tic-Tac-Toe
- **Card Games** - Poker, Bridge strategy
- **Video Game AI** - Turn-based strategy games
- **Decision Theory** - Competitive scenarios
- **Resource Allocation** - Zero-sum negotiations
- **Financial Trading** - Adversarial market strategies

### ✂️ Alpha-Beta Pruning Applications
- **Real-time Gaming** - Fast move calculation
- **Chess Engines** - Deep position analysis
- **Game Tree Search** - Efficient exploration
- **AI Competitions** - Tournament play
- **Strategic Planning** - Military/business strategy
- **Optimization Problems** - Adversarial optimization

### 🎮 Interactive Gaming Applications
- **Educational Tools** - Algorithm demonstration
- **Game Development** - AI opponent creation
- **Strategy Testing** - Algorithm comparison
- **User Interfaces** - Human-AI interaction
- **Prototype Development** - Game logic testing

## ⚡ Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Pruning Efficiency | Optimal? | Complete? |
|-----------|----------------|------------------|-------------------|----------|-----------|
| **MinMax** 🎯 | O(b^d) | O(d) | None | ✅ Yes | ✅ Yes |
| **Alpha-Beta** ✂️ | O(b^(d/2))* | O(d) | Up to 50% | ✅ Yes | ✅ Yes |

**Legend:**
- `b` = Branching factor (possible moves per position)
- `d` = Maximum depth of game tree
- `*` = Best case with optimal move ordering

**Performance Characteristics:**
- **MinMax**: Exhaustive but complete optimal solution
- **Alpha-Beta**: Same optimality with significantly faster execution

**Tic-Tac-Toe Specifics:**
- Maximum depth: 9 moves
- Branching factor: 9 to 1 (decreasing)
- Total positions: ~362,880 (9!)
- Alpha-Beta reduces to ~10,000 evaluations

## 📸 Input & Output Examples

### 🔧 Input Game State
```
Tic-Tac-Toe Board:
 X |   | O 
-----------
   | X |   
-----------
 O |   |   

Current Player: AI (X)
Evaluation: AI calculating optimal move...
```

### 📊 Sample Outputs

<img width="1492" alt="minimaxAB" src="https://github.com/user-attachments/assets/0d1894f6-ed20-45d9-9369-a150c84bd98e" />


## 🛠️ Usage

### Basic Game Setup
```python
# Create game instance
game = MinMaxAlphaBeta()

# Initialize empty 3x3 board
board = [[' ' for _ in range(3)] for _ in range(3)]

# Set players
# 'X' = AI (maximizing player)
# 'O' = Human (minimizing player)
```

### Algorithm Usage
```python
# Use MinMax algorithm
score = game.min_max(board, depth=0, is_maximizing=True)

# Use Alpha-Beta pruning (recommended)
score = game.alpha_beta(board, depth=0, is_maximizing=True, 
                       alpha=-float('inf'), beta=float('inf'))

# Get best move for AI
best_move = game.get_best_move(board, is_maximizing=True)

# Make a move
new_board = game.make_move(board, best_move, 'X')
```

### Interactive Game Play
```python
# Run the complete interactive game
python minimax_alphabeta.py

# Game flow:
# 1. Human enters move (row, col)
# 2. AI calculates optimal response
# 3. Board updates and displays
# 4. Repeat until win/draw
```

## 🔍 Algorithm Comparison

| Feature | MinMax 🎯 | Alpha-Beta ✂️ |
|---------|-----------|---------------|
| **Search Strategy** | Complete tree exploration | Pruned tree exploration |
| **Time Complexity** | O(b^d) | O(b^(d/2)) best case |
| **Space Complexity** | O(d) | O(d) |
| **Optimality** | Guaranteed | Guaranteed |
| **Practical Speed** | Slower | Much faster |
| **Implementation** | Simpler | Slightly complex |

## 🏗️ Implementation Features

### Core Components
- ✅ **Game State Management** - Board representation and manipulation
- ✅ **Move Generation** - All possible legal moves
- ✅ **Win Detection** - Complete victory condition checking
- ✅ **Recursive Search** - Full game tree exploration
- ✅ **Optimal Decision** - Best move selection

### Advanced Features
- 🎯 **Depth-Limited Search** - Configurable search depth
- ✂️ **Pruning Optimization** - Alpha-beta branch elimination
- 🎮 **Interactive Interface** - Human vs AI gameplay
- 📊 **Board Visualization** - Clear game state display
- 🔄 **Turn Management** - Alternating player moves

### Game-Specific Features
- 🏆 **Win Conditions** - Rows, columns, diagonals
- 🤝 **Draw Detection** - Board full without winner
- 🎪 **Input Validation** - Error handling for user moves
- 🤖 **AI Intelligence** - Perfect play guarantee
- 👤 **Human Interface** - Intuitive move input

## 📚 Requirements

```python
# No external dependencies required!
# Built with Python's standard library
```

Pure Python implementation - no external dependencies! 🎉

## 🎯 Key Advantages & Strategies

### 🎯 MinMax Advantages
- **Perfect Play**: Guarantees optimal moves
- **Complete Search**: Explores all possibilities
- **Theoretical Foundation**: Solid game theory basis
- **Predictable Behavior**: Deterministic outcomes

### ✂️ Alpha-Beta Advantages
- **Efficiency**: Dramatic speed improvement
- **Same Optimality**: No loss in decision quality
- **Scalability**: Handles deeper searches
- **Practical Viability**: Real-time game applications

### 🎮 Game Design Benefits
- **Educational Value**: Clear algorithm demonstration
- **Interactive Learning**: Hands-on experience
- **Perfect Opponent**: Challenging gameplay
- **Algorithm Comparison**: Performance testing

## 🚨 Important Notes

### Performance Considerations
- **Move Ordering**: Better ordering improves Alpha-Beta efficiency
- **Depth Limits**: Deeper search = better play but slower execution
- **Evaluation Functions**: For complex games, need position evaluation
- **Memory Usage**: Recursive calls use stack space

### Implementation Details
- **Player Representation**: 'X' for AI, 'O' for human
- **Board Indexing**: 0-based (0,0) to (2,2)
- **Empty Cells**: Represented by space character ' '
- **Win Values**: +1 for AI win, -1 for human win, 0 for draw

### Game Theory Insights
- **Zero-Sum Nature**: One player's gain = other's loss
- **Perfect Information**: All game state visible to both players
- **Finite Game Tree**: Tic-Tac-Toe has limited depth
- **Optimal Play**: Both algorithms guarantee best possible moves

## 🔄 Extensions & Variations

### Algorithm Enhancements
- **Iterative Deepening**: Progressive depth increase
- **Transposition Tables**: Memoization for repeated positions
- **Move Ordering**: Heuristic-based move prioritization
- **Quiescence Search**: Extending search at critical positions

### Game Variations
- **Connect Four**: Vertical drop game
- **Othello/Reverso**: Disk flipping strategy
- **Chess**: Complex piece movement
- **Checkers**: Diagonal movement and capturing

### Advanced Features
- **Time Limits**: Real-time move constraints
- **Difficulty Levels**: Adjustable search depth
- **Opening Books**: Pre-computed optimal openings
- **Endgame Tables**: Perfect play databases

---

*Master the art of strategic thinking with perfect game-playing algorithms!* 🏆🧠