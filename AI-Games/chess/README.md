# 🧠 Chess Game - Human vs AI

A fully functional chess game built with React and Next.js, featuring an intelligent AI opponent powered by the minimax algorithm with alpha-beta pruning.

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

Before running this chess game, make sure you have the following software installed on your system:

### 🛠️ Required Software
- **Node.js** (version 16.0 or higher)  
  - Download from [nodejs.org](https://nodejs.org/)  
  - Verify installation: `node --version`
- **npm** (comes with Node.js) or **yarn**  
  - Verify npm: `npm --version`  
  - Or install yarn: `npm install -g yarn`

### 📦 Required Libraries/Frameworks
This project uses the following technologies:
- **Next.js** (React framework)
- **Tailwind CSS** (for styling)

All dependencies will be automatically installed during setup.

## ⚙️ Installation & Setup

1. **📥 Clone the repository:**
   ```bash
   git clone https://github.com/tsrohit99/AI-Course.git
   cd AI-Course/AI-Games/chess
   ```

2. **📦 Install dependencies:**
   ```bash
   npm install
   # or
   yarn install
   ```

## 🚀 How to Run

1. **🏃‍♂️ Start the development server:**
   ```bash
   npm run dev
   # or
   yarn dev
   ```

2. **🌐 Open your browser:**
   - Navigate to `http://localhost:3000`
   - The chess game should load automatically

3. **🏗️ Build for production (optional):**
   ```bash
   npm run build
   npm start
   # or
   yarn build
   yarn start
   ```

## 🎮 How to Play

### 📋 Game Rules
This chess game follows traditional chess rules with one key simplification: **the game ends when a king is captured** (rather than checkmate).

### 🎯 Playing the Game

#### 🎛️ Basic Controls
1. **You play as White pieces** (bottom of the board)
2. **AI plays as Black pieces** (top of the board)
3. **White always moves first**

#### ♟️ Making Moves
1. **🖱️ Select a piece:** Click on any of your white pieces
   - The selected piece will be highlighted in green
   - Valid moves will be highlighted in blue

2. **➡️ Move the piece:** Click on any blue-highlighted square
   - The piece will move to that position
   - If there's an opponent piece there, it will be captured

3. **❌ Invalid moves:** Clicking on a non-highlighted square will deselect your piece

#### 🏰 Piece Movement Rules
- **♙ Pawn:** Moves forward one square, captures diagonally. Can move two squares from starting position
- **♖ Rook:** Moves horizontally or vertically any number of squares
- **♘ Knight:** Moves in an L-shape (2+1 squares)
- **♗ Bishop:** Moves diagonally any number of squares
- **♕ Queen:** Combines rook and bishop movements
- **♔ King:** Moves one square in any direction

#### 🏆 Win Conditions
- **🎉 You win:** Capture the AI's black king (♚)
- **🤖 AI wins:** AI captures your white king (♔)
- The game displays the winner and offers a "New Game" button

#### 🖥️ Game Interface
- **🔄 Turn indicator:** Shows whose turn it is
- **🤔 AI thinking:** Shows "AI Thinking..." with a spinning emoji when AI is calculating
- **📊 Game status:** Displays win/loss messages
- **🆕 New game button:** Appears after game ends to restart

## 📸 Game Screenshots

### 🎬 Game Start
<img width="1043" alt="start" src="https://github.com/user-attachments/assets/973be9ff-4e37-47fc-b7b1-c62c115a9b56" />


*Initial game setup with all pieces in starting positions*

### 🎯 Piece Selection
<img width="1041" alt="direction" src="https://github.com/user-attachments/assets/7ef47be0-0307-4db6-b348-ca76751f15c2" />
*Selected white piece (green highlight) with valid moves shown in blue*


### 🏁 Game Over
<img width="1044" alt="end" src="https://github.com/user-attachments/assets/55893715-9f96-43e6-9d15-0ef7b7cdb949" />
*End game screen showing winner and New Game button*

## 🧮 Algorithm & Technical Details

### 🤖 AI Algorithm: Minimax with Alpha-Beta Pruning

The AI opponent uses a sophisticated decision-making algorithm:

#### 1️⃣ Minimax Algorithm
- **🎯 Purpose:** Evaluates all possible moves to find the best one
- **📏 Depth:** Looks 3 moves ahead (configurable)
- **🧠 Strategy:** Assumes both players play optimally

#### 2️⃣ Alpha-Beta Pruning
- **⚡ Optimization:** Eliminates branches that won't affect the final decision
- **🚀 Performance:** Significantly reduces computation time
- **⏱️ Efficiency:** Allows deeper search within reasonable time limits

#### 3️⃣ Board Evaluation Function
The AI evaluates positions based on:
- **⚖️ Material balance:** Point values for pieces
  - Pawn: 1 point
  - Knight/Bishop: 3 points
  - Rook: 5 points
  - Queen: 9 points
  - King: 100 points
- **👑 King safety:** Massive bonus for capturing opponent's king
- **📍 Position advantages:** (can be extended for more sophisticated play)

#### 4️⃣ Algorithm Flow
```
1. Generate all possible moves for AI (black pieces)
2. For each move:
   a. Apply move to create new board state
   b. Recursively evaluate opponent's best response
   c. Continue for specified depth
3. Choose move with highest evaluation score
4. Execute the selected move
```

### 💻 Technical Implementation

#### 🔧 Key Components
- **⚛️ React State Management:** Manages game state, board position, and UI
- **🎯 Move Generation:** Calculates valid moves for each piece type
- **✅ Move Validation:** Ensures moves follow chess rules
- **🎮 Game Logic:** Handles turn switching, win detection, and game flow

#### ⚡ Performance Optimizations
- **🔄 useCallback:** Prevents unnecessary re-renders of AI function
- **🗂️ Efficient board representation:** 8x8 array for fast access
- **✂️ Minimax pruning:** Reduces search space significantly
- **🔄 Async AI moves:** Non-blocking UI during AI calculation

## ✨ Features

### 🎯 Core Features
- ✅ **♟️ Complete chess piece movement** (all 6 piece types)
- ✅ **🧠 Intelligent AI opponent** with minimax algorithm
- ✅ **👁️ Visual move indicators** (selection and valid moves)
- ✅ **🔄 Turn-based gameplay** with clear status display
- ✅ **🏆 Win/loss detection** with king capture
- ✅ **🔄 Game reset functionality**

### 🎨 UI/UX Features
- ✅ **📱 Responsive design** works on different screen sizes
- ✅ **👀 Visual feedback** for piece selection and moves
- ✅ **🖱️ Hover effects** for better interactivity
- ✅ **🤔 AI thinking indicator** shows when AI is calculating
- ✅ **🎨 Clean, modern design** with chess-themed colors

### 🔧 Technical Features
- ✅ **⚡ Optimized performance** with React best practices
- ✅ **🛡️ Type-safe implementation** (can be enhanced with TypeScript)
- ✅ **🧩 Modular code structure** for easy maintenance
- ✅ **⚙️ Configurable AI difficulty** (depth parameter)

## 📁 Project Structure

```
AI-Course/
└── AI-Games/
    └── chess/
        ├── src/
        │   ├── app/
        │   │   ├── page.js          # Main chess game component
        │   │   ├── layout.js        # App layout
        │   │   └── globals.css      # Global styles
        ├── public/                  # Static assets
        ├── package.json            # Dependencies and scripts
        ├── tailwind.config.js      # Tailwind CSS configuration
        ├── next.config.js          # Next.js configuration
        └── README.md              # This file
```

## 🔮 Future Enhancements

Potential improvements for the chess game:

- **📜 Advanced Rules:** Implement castling, en passant, pawn promotion
- **🔒 Checkmate Detection:** Replace king capture with proper checkmate logic
- **📝 Move History:** Track and display all moves made
- **🎚️ Difficulty Levels:** Multiple AI difficulty settings
- **🌐 Online Multiplayer:** Player vs player functionality
- **📊 Game Analysis:** Show best moves and analysis
- **💾 Save/Load Games:** Persist game state
- **🏆 Tournament Mode:** Multiple games tracking

## 🐞 Troubleshooting

### ⚠️ Common Issues

1. **🚫 Game doesn't load:**
   - Ensure Node.js is installed (`node --version`)
   - Check if you're in the correct directory (`AI-Course/AI-Games/chess`)
   - Verify dependencies are installed (`npm install`)
   - Check if development server is running (`npm run dev`)
   - Verify you're accessing `http://localhost:3000`

2. **🎨 Styling issues:**
   - Ensure Tailwind CSS is properly configured
   - Check if `globals.css` imports Tailwind directives

3. **🤖 AI not moving:**
   - Check browser console for JavaScript errors
   - Ensure the game state allows AI moves (black's turn, game playing)

4. **🐌 Performance issues:**
   - Reduce AI search depth in minimax function
   - Check for infinite loops in move generation

### 🆘 Getting Help

If you encounter any issues:
1. 🔍 Check the browser console for error messages
2. ✅ Verify all dependencies are installed correctly
3. 🔄 Ensure you're using a compatible Node.js version
4. 🔄 Try restarting the development server

---

---
**🎉 Enjoy playing chess against the AI! 🏆**