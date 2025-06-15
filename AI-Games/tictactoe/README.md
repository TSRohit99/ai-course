# ⭕ Tic-Tac-Toe Game - Human vs AI

A classic Tic-Tac-Toe game implemented in Python featuring an unbeatable AI opponent powered by the minimax algorithm. Challenge yourself against an AI that never loses!

## 📑 Table of Contents
- [🧰 Prerequisites](#-prerequisites)
- [⚙️ Installation & Setup](#️-installation--setup)
- [🚀 How to Run](#-how-to-run)
- [🎮 How to Play](#-how-to-play)
- [📸 Game Screenshots](#-game-screenshots)
- [🧮 Algorithm & Technical Details](#-algorithm--technical-details)
- [✨ Features](#-features)
- [📁 Project Structure](#-project-structure)
- [🔮 Future Enhancements](#-future-enhancements)
- [🐞 Troubleshooting](#-troubleshooting)

## 🧰 Prerequisites

Before running this Tic-Tac-Toe game, make sure you have the following software installed on your system:

### 🐍 Required Software
- **Python** (version 3.6 or higher)  
  - Download from [python.org](https://www.python.org/)  
  - Verify installation: `python --version` or `python3 --version`

### 📦 Required Libraries
This game uses only Python's built-in libraries:
- **math** (for infinity values in minimax algorithm)

No additional packages need to be installed!

## ⚙️ Installation & Setup

1. **📥 Clone the repository:**
   ```bash
   git clone https://github.com/tsrohit99/AI-Course.git
   cd AI-Course/AI-Games/tictactoe
   ```

2. **✅ Verify Python installation:**
   ```bash
   python --version
   # or
   python3 --version
   ```

That's it! No additional setup required.

## 🚀 How to Run

1. **🏃‍♂️ Navigate to the game directory:**
   ```bash
   cd AI-Course/AI-Games/tictactoe
   ```

2. **▶️ Run the game:**
   ```bash
   python tictactoe.py
   # or
   python3 tictactoe.py
   ```

3. **🎮 Start playing:**
   - The game will display the board and prompt for your move
   - Follow the on-screen instructions to play

## 🎮 How to Play

### 📋 Game Rules
This is a classic Tic-Tac-Toe game following traditional rules:
- **Goal:** Get three of your marks in a row (horizontally, vertically, or diagonally)
- **Players:** You (X) vs AI (O)
- **Turns:** Players alternate turns
- **Winner:** First to get three in a row wins
- **Draw:** If the board fills up with no winner, it's a tie

### 🎯 Playing the Game

#### 🎛️ Basic Controls
1. **You play as X** (human player)
2. **AI plays as O** (computer opponent)
3. **X always goes first** (you start)

#### 🎲 Making Your Move
1. **📍 Board positions:** The board uses positions 1-9:
   ```
   1|2|3
   -+-+-
   4|5|6
   -+-+-
   7|8|9
   ```

2. **⌨️ Input your move:** Type a number from 1-9 when prompted
   - Example: Type `5` to place your X in the center

3. **✅ Valid moves:** Only empty positions are allowed
   - The game will tell you if a spot is already taken

4. **🤖 AI turn:** After your move, the AI will automatically make its move

#### 🏆 Win Conditions
- **🎉 You win:** Get three X's in a row
- **🤖 AI wins:** AI gets three O's in a row  
- **🤝 Draw:** Board is full with no winner

#### 🖥️ Game Interface
- **📊 Board display:** Shows current state after each move
- **💭 AI thinking:** Shows "AI thinking..." before AI moves
- **📢 Game result:** Displays winner or draw at the end
- **🔄 Restart:** Run the program again to play another game

## 📸 Game Screenshots

<img width="1512" alt="tictactoe" src="https://github.com/user-attachments/assets/f195a132-2128-4837-bfc8-d553105eeebf" />
*Terminal*

## 🧮 Algorithm & Technical Details

### 🤖 AI Algorithm: Minimax

The AI opponent uses the minimax algorithm to make optimal decisions:

#### 🧠 Minimax Algorithm
- **🎯 Purpose:** Evaluates all possible game outcomes to find the best move
- **📊 Strategy:** Assumes both players play optimally
- **🏆 Guarantee:** The AI will never lose (only win or draw)

#### 🔄 How Minimax Works
1. **🌳 Game Tree:** Explores all possible future game states
2. **📊 Scoring:** Assigns values to terminal states:
   - AI Win (O): +1 point
   - Human Win (X): -1 point  
   - Draw: 0 points
3. **⚖️ Decision Making:**
   - **Maximizing:** AI chooses moves that maximize its score
   - **Minimizing:** Assumes human chooses moves that minimize AI's score

#### 🔍 Algorithm Flow
```
For each possible move:
1. Make the move on the board
2. Recursively evaluate all possible responses
3. Assign a score based on the best outcome
4. Undo the move
5. Choose the move with the highest score
```

### 💻 Technical Implementation

#### 🏗️ Key Components
- **🎯 Board Representation:** 9-element list representing the 3x3 grid
- **🏆 Winner Detection:** Checks all winning combinations after each move
- **🤖 AI Logic:** Implements minimax to find optimal moves
- **👤 Human Interface:** Handles user input and validation

#### 📊 Data Structures
- **Board:** `[' ']*9` - List representing positions 0-8
- **Winning Combinations:** Tuples of positions that form winning lines
- **Game States:** 'X', 'O', 'Tie', or None for ongoing games

#### ⚡ Performance Features
- **🎯 Efficient Evaluation:** Quick winner detection using predefined patterns
- **🔄 State Management:** Temporary moves for evaluation, then undo
- **⚡ Optimized Search:** Minimax explores only necessary game states

## ✨ Features

### 🎯 Core Features
- ✅ **🎮 Classic Tic-Tac-Toe gameplay** with traditional rules
- ✅ **🧠 Unbeatable AI opponent** using minimax algorithm
- ✅ **👤 Human vs AI** interactive gameplay
- ✅ **🏆 Win/loss/draw detection** with clear results
- ✅ **📍 Position-based input** (1-9 grid system)

### 🎨 UI/UX Features
- ✅ **📊 Clear board visualization** with ASCII art
- ✅ **💭 AI thinking indicator** shows when AI is calculating
- ✅ **⚠️ Input validation** prevents invalid moves
- ✅ **📢 Clear game feedback** for all game states
- ✅ **🎯 Simple controls** with numbered positions

### 🔧 Technical Features
- ✅ **🐍 Pure Python implementation** no external dependencies
- ✅ **🧮 Optimal AI algorithm** guarantees best play
- ✅ **🛡️ Error handling** for invalid inputs
- ✅ **🎯 Efficient code structure** with modular functions
- ✅ **💾 Lightweight** minimal resource usage

## 📁 Project Structure

```
AI-Course/
└── AI-Games/
    └── tictactoe/
        ├── tictactoe.py        # Main game file
        └── README.md           # This documentation
```

### 📋 Code Organization
- **🎮 Game Logic:** Winner detection and game flow
- **🎨 Display Functions:** Board visualization
- **🤖 AI Implementation:** Minimax algorithm
- **👤 User Interface:** Input handling and validation

## 🔮 Future Enhancements

Potential improvements for the Tic-Tac-Toe game:

### 🎮 Gameplay Enhancements
- **🎚️ Difficulty Levels:** Add easier AI modes for beginners
- **👥 Two-Player Mode:** Human vs Human option
- **📊 Score Tracking:** Keep track of wins/losses across games
- **⏱️ Timed Moves:** Add time limits for moves

### 🎨 Interface Improvements
- **🖼️ GUI Version:** Create a graphical interface with tkinter
- **🎨 Colorful Display:** Add colors to the terminal output
- **🎵 Sound Effects:** Add audio feedback for moves and wins
- **📱 Mobile Version:** Create a mobile-friendly version

### 🔧 Technical Enhancements
- **💾 Game History:** Save and replay games
- **📈 Statistics:** Track performance statistics
- **🔄 Undo/Redo:** Allow players to undo moves
- **🎯 Move Hints:** Show optimal moves for learning

### 🌐 Advanced Features
- **🌍 Online Multiplayer:** Play against other humans online
- **🤖 Different AI Personalities:** Various AI playing styles
- **📚 Learning Mode:** Tutorial for new players
- **🏆 Tournament Mode:** Multiple game tournaments

## 🐞 Troubleshooting

### ⚠️ Common Issues

1. **🐍 Python not found:**
   ```bash
   python: command not found
   ```
   - **Solution:** Install Python from [python.org](https://www.python.org/)
   - **Alternative:** Try `python3` instead of `python`

2. **❌ Invalid input errors:**
   ```
   Invalid input.
   ```
   - **Solution:** Enter only numbers 1-9
   - **Tip:** Make sure the position isn't already taken

3. **🚫 Spot taken error:**
   ```
   Spot taken!
   ```
   - **Solution:** Choose a different position (1-9)
   - **Tip:** Look at the board to see available spaces

4. **🔄 Game won't restart:**
   - **Solution:** Run the program again: `python tictactoe.py`
   - **Tip:** The game ends after each match

### 🆘 Getting Help

If you encounter any issues:

1. **🔍 Check Python installation:**
   ```bash
   python --version
   ```

2. **📁 Verify file location:**
   - Make sure you're in the correct directory
   - Check that `tictactoe.py` exists

3. **🔄 Try different Python command:**
   ```bash
   python3 tictactoe.py
   ```

4. **🐛 Check for typos:**
   - Ensure you're entering numbers 1-9
   - Verify the filename is correct

### 💡 Pro Tips
- **🎯 Strategy:** Try to block the AI while setting up your own winning moves
- **🧠 Learning:** Watch the AI's moves to understand optimal play
- **🔄 Practice:** Play multiple games to improve your skills
- **📖 Study:** Learn Tic-Tac-Toe strategy to maximize your draws against the AI

---

**🎉 Challenge the unbeatable AI and see if you can achieve a draw! 🏆**