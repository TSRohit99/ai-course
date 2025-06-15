# 🧠 Rock-Paper-Scissors with AI Strategy

A command-line Rock-Paper-Scissors game written in Python, where you play against an intelligent AI that adapts and learns from your move patterns. The AI starts randomly but becomes increasingly strategic as it analyzes your gameplay history!

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

Before running this Rock-Paper-Scissors game, make sure you have the following software installed on your system:

### 🐍 Required Software
- **Python** (version 3.6 or higher)  
  - Download from [python.org](https://www.python.org/)  
  - Verify installation: `python --version` or `python3 --version`

### 📦 Required Libraries
This game uses only Python's built-in libraries:
- **random** (for initial AI randomization and game mechanics)

No additional packages need to be installed!

## ⚙️ Installation & Setup

1. **📥 Clone the repository:**
   ```bash
   git clone https://github.com/tsrohit99/AI-Course.git
   cd AI-Course/AI-Games/smart-rps
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
   cd AI-Course/AI-Games/smart-rps
   ```

2. **▶️ Run the game:**
   ```bash
   python smartRPS.py
   # or
   python3 smartRPS.py
   ```

3. **🎮 Start playing:**
   - The game will display instructions and prompt for your move
   - Follow the on-screen prompts to play against the AI

## 🎮 How to Play

### 📋 Game Rules
This follows the classic Rock-Paper-Scissors rules with an intelligent twist:
- **🪨 Rock** beats **✂️ Scissors**
- **📄 Paper** beats **🪨 Rock**
- **✂️ Scissors** beats **📄 Paper**
- **Same moves** result in a tie
- **AI learns** from your patterns and adapts its strategy

### 🎯 Playing the Game

#### 🎛️ Basic Controls
1. **Choose your move:** Enter 'rock', 'paper', or 'scissors'
2. **AI responds:** The AI will make its move based on its strategy
3. **See results:** View the outcome and running score
4. **Continue playing:** Keep playing to see the AI adapt to your patterns

#### ⌨️ Input Options
- **🪨 Rock:** Type `rock`, `r`, or `1`
- **📄 Paper:** Type `paper`, `p`, or `2`
- **✂️ Scissors:** Type `scissors`, `s`, or `3`
- **🚪 Quit:** Type `quit` or `q` to exit the game

#### 🤖 AI Behavior Phases
1. **🎲 Learning Phase (Rounds 1-3):** AI plays randomly to gather data
2. **🧠 Strategic Phase (Round 4+):** AI analyzes your patterns and counters your most frequent move

#### 🏆 Scoring System
- **Win:** +1 point to your score
- **Loss:** +1 point to AI's score
- **Tie:** No points awarded
- **Statistics:** Track your move frequency and AI's adaptation

#### 🖥️ Game Interface
- **📊 Move prompt:** Clear input instructions
- **🎯 Result display:** Shows both moves and outcome
- **📈 Running score:** Current win/loss/tie count
- **🤔 AI reasoning:** Explains AI's decision-making process
- **📊 Final statistics:** Summary of all moves and patterns

## 📸 Game Screenshots
<img width="1512" alt="rps" src="https://github.com/user-attachments/assets/64bd5c3c-f2d8-42ee-9b4f-6e8cd53c3300" />
*Terminal*



## 🧮 Algorithm & Technical Details

### 🤖 AI Strategy: Adaptive Pattern Recognition

The AI uses a two-phase learning approach to become increasingly competitive:

#### 🎲 Phase 1: Random Learning (Rounds 1-3)
- **🎯 Purpose:** Gather initial data about player preferences
- **🎲 Strategy:** Play completely random moves
- **📊 Data Collection:** Track frequency of player's rock, paper, scissors

#### 🧠 Phase 2: Counter-Strategy (Round 4+)
- **📈 Analysis:** Identify player's most frequently used move
- **🎯 Counter-Logic:** Choose the move that beats the player's favorite
- **⚖️ Adaptation:** Continuously update strategy as new data comes in

#### 🔄 Algorithm Flow
```
1. Track player move frequency in a dictionary
2. If round <= 3:
   - Play random move
   - Update player statistics
3. If round > 3:
   - Find player's most common move
   - Select counter-move (rock→paper, paper→scissors, scissors→rock)
   - Explain reasoning to player
4. Compare moves and update score
```

### 💻 Technical Implementation

#### 🏗️ Key Components
- **📊 Move Tracking:** Dictionary storing frequency of each player move
- **🎲 Random Generator:** Initial random move selection
- **🧮 Counter Logic:** Mapping each move to its counter
- **📈 Statistics Engine:** Real-time analysis of player patterns

#### 📊 Data Structures
- **Player Moves:** `{'rock': count, 'paper': count, 'scissors': count}`
- **Counter Map:** `{'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}`
- **Game State:** Round number, scores, move history

#### ⚡ Performance Features
- **🎯 Efficient Tracking:** O(1) move frequency updates
- **🧠 Smart Analysis:** Quick identification of most common move
- **💾 Memory Efficient:** Minimal data storage requirements
- **⚡ Real-time Adaptation:** Instant strategy updates after each round

## ✨ Features

### 🎯 Core Features
- ✅ **🎮 Classic Rock-Paper-Scissors** with traditional rules
- ✅ **🧠 Adaptive AI opponent** that learns from your patterns
- ✅ **📈 Two-phase AI strategy** (random learning → counter-strategy)
- ✅ **📊 Real-time statistics** showing your move patterns
- ✅ **🎯 Strategic explanations** of AI decision-making

### 🎨 UI/UX Features
- ✅ **📱 Multiple input formats** (full words, letters, numbers)
- ✅ **🎨 Clear game display** with emojis and formatting
- ✅ **📊 Running score tracking** throughout the game
- ✅ **🤔 AI reasoning display** explains strategy decisions
- ✅ **📈 Detailed end statistics** with move distribution

### 🔧 Technical Features
- ✅ **🐍 Pure Python implementation** no external dependencies
- ✅ **🧮 Pattern recognition algorithm** tracks and analyzes behavior
- ✅ **🛡️ Input validation** handles various input formats
- ✅ **📊 Comprehensive statistics** tracking and reporting
- ✅ **💾 Lightweight design** minimal resource usage

### 🎓 Educational Features
- ✅ **🧠 AI strategy explanation** teaches machine learning concepts
- ✅ **📈 Pattern visualization** shows how AI learns
- ✅ **🎯 Strategy awareness** helps players understand their own patterns
- ✅ **🤖 Adaptive demonstration** shows real-time AI learning

## 📁 Project Structure

```
AI-Course/
└── AI-Games/
    └── smart-rps/
        ├── smartRPS.py         # Main game file with AI logic
        └── README.md           # This documentation
```

### 📋 Code Organization
- **🎮 Game Logic:** Core Rock-Paper-Scissors mechanics
- **🧠 AI Strategy:** Pattern recognition and counter-strategy
- **📊 Statistics Tracking:** Move frequency and game analysis
- **👤 User Interface:** Input handling and display formatting

## 🔮 Future Enhancements

Potential improvements for the Smart Rock-Paper-Scissors game:

### 🤖 AI Improvements
- **🧠 Advanced Pattern Recognition:** Implement Markov chains for sequence analysis
- **📊 Multiple Strategy Modes:** Add different AI personalities and difficulty levels
- **🎯 Meta-Learning:** AI that adapts to counter-counter strategies
- **📈 Long-term Memory:** Save and learn from previous game sessions

### 🎮 Gameplay Enhancements
- **👥 Multiplayer Mode:** Human vs Human option
- **🏆 Tournament System:** Best-of-X matches with rankings
- **⏱️ Timed Rounds:** Add time pressure for quick decisions
- **🎖️ Achievement System:** Unlock rewards for different play patterns

### 🎨 Interface Improvements
- **🖼️ GUI Version:** Create graphical interface with tkinter/pygame
- **🌈 Colorful Terminal:** Add colors and better ASCII art
- **📱 Web Version:** Browser-based game with HTML/CSS/JavaScript
- **🎵 Sound Effects:** Audio feedback for moves and outcomes

### 📊 Advanced Analytics
- **📈 Detailed Statistics:** Win rate analysis, streak tracking
- **🎯 Strategy Recommendations:** Suggest optimal counter-strategies
- **📊 Visualization:** Graphs showing pattern evolution over time
- **💾 Data Export:** Save game data for external analysis

### 🌐 Extended Features
- **🌍 Online Multiplayer:** Play against other humans worldwide
- **📚 Tutorial Mode:** Interactive learning for optimal strategies
- **🤖 AI vs AI Mode:** Watch different AI strategies compete
- **📖 Strategy Library:** Learn about different RPS strategies

## 🐞 Troubleshooting

### ⚠️ Common Issues

1. **🐍 Python not found:**
   ```bash
   python: command not found
   ```
   - **Solution:** Install Python from [python.org](https://www.python.org/)
   - **Alternative:** Try `python3` instead of `python`

2. **❌ Invalid input handling:**
   ```
   Invalid input! Please enter rock, paper, scissors.
   ```
   - **Solution:** Use accepted input formats:
     - Full words: `rock`, `paper`, `scissors`


### 🆘 Getting Help

If you encounter any issues:

1. **🔍 Check Python installation:**
   ```bash
   python --version
   python3 --version
   ```

2. **📁 Verify file location:**
   - Make sure you're in the correct directory
   - Check that `smartRPS.py` exists in the smart-rps folder

3. **🔄 Try different Python command:**
   ```bash
   python3 smartRPS.py
   ```

4. **🐛 Check file permissions:**
   ```bash
   ls -la smartRPS.py
   ```

### 💡 Pro Tips

#### 🎯 Strategy Tips
- **🎲 Be unpredictable:** Vary your moves to confuse the AI
- **📊 Watch patterns:** Notice when the AI switches from random to strategic
- **🧠 Counter the counter:** Once AI adapts, change your most frequent move
- **🎯 Test the AI:** Play predictably at first, then switch strategies

#### 🎮 Gameplay Tips
- **📈 Track your own patterns:** Be aware of your move tendencies
- **🤖 Learn from AI:** Watch how it adapts to understand pattern recognition
- **🔄 Play multiple sessions:** See how quickly the AI learns each time
- **📊 Analyze end statistics:** Use the final report to improve your strategy

#### 🧠 Learning Opportunities
- **🎓 Understand AI learning:** This demonstrates basic machine learning concepts
- **📊 Pattern recognition:** Learn how frequency analysis works
- **🤖 Counter-strategies:** Understand how AI can adapt to human behavior
- **🎯 Game theory:** Explore optimal strategies in competitive games

---

**🎉 Challenge the adaptive AI and see if you can outsmart its learning algorithm! 🤖✊📄✂️**