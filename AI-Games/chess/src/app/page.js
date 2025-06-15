"use client";
import React, { useState, useEffect, useCallback } from 'react';

/**
 * ChessGame Component
 * A complete chess game implementation with AI opponent using minimax algorithm
 * Features:
 * - Human vs AI gameplay (Human plays white, AI plays black)
 * - Complete chess piece movement logic
 * - Visual feedback for selected pieces and valid moves
 * - Game ends when a king is captured (simplified chess rules)
 */
const ChessGame = () => {
  /**
   * Unicode symbols for chess pieces
   * Uppercase letters represent white pieces, lowercase represent black pieces
   * White pieces: ♔♕♖♗♘♙ (King, Queen, Rook, Bishop, Knight, Pawn)
   * Black pieces: ♚♛♜♝♞♟ (King, Queen, Rook, Bishop, Knight, Pawn)
   */
  const pieces = {
    'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙', // White pieces
    'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'  // Black pieces
  };

  /**
   * Initial chess board setup in standard starting position
   * 8x8 grid where:
   * - Row 0: Black back rank (rook, knight, bishop, queen, king, bishop, knight, rook)
   * - Row 1: Black pawns
   * - Rows 2-5: Empty squares (null)
   * - Row 6: White pawns
   * - Row 7: White back rank
   */
  const initialBoard = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], // Black pieces
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], // Black pawns
    [null, null, null, null, null, null, null, null], // Empty row
    [null, null, null, null, null, null, null, null], // Empty row
    [null, null, null, null, null, null, null, null], // Empty row
    [null, null, null, null, null, null, null, null], // Empty row
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'], // White pawns
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']  // White pieces
  ];

  // ============================================================================
  // STATE MANAGEMENT
  // ============================================================================

  /** Current state of the chess board - 8x8 array of pieces or null */
  const [board, setBoard] = useState(initialBoard);
  
  /** Current player's turn - 'white' for human player, 'black' for AI */
  const [currentPlayer, setCurrentPlayer] = useState('white');
  
  /** Currently selected square coordinates [row, col] or null if no selection */
  const [selectedSquare, setSelectedSquare] = useState(null);
  
  /** Array of valid move coordinates [[row, col], ...] for the selected piece */
  const [validMoves, setValidMoves] = useState([]);
  
  /** Game status: 'playing', 'white-wins', 'black-wins' */
  const [gameStatus, setGameStatus] = useState('playing');
  
  /** Flag to show when AI is calculating its move */
  const [isThinking, setIsThinking] = useState(false);

  // ============================================================================
  // UTILITY FUNCTIONS FOR PIECE AND POSITION VALIDATION
  // ============================================================================

  /**
   * Check if a piece is white (uppercase letters represent white pieces)
   * @param {string|null} piece - The piece character or null
   * @returns {boolean} True if piece is white
   */
  const isWhitePiece = (piece) => piece && piece === piece.toUpperCase();

  /**
   * Check if a piece is black (lowercase letters represent black pieces)
   * @param {string|null} piece - The piece character or null
   * @returns {boolean} True if piece is black
   */
  const isBlackPiece = (piece) => piece && piece === piece.toLowerCase();

  /**
   * Validate if board coordinates are within the 8x8 chess board
   * @param {number} row - Row coordinate (0-7)
   * @param {number} col - Column coordinate (0-7)
   * @returns {boolean} True if position is valid
   */
  const isValidPosition = (row, col) => row >= 0 && row < 8 && col >= 0 && col < 8;

  /**
   * Check if a piece belongs to the opponent
   * @param {string|null} piece - The piece to check
   * @param {string} playerColor - Current player color ('white' or 'black')
   * @returns {boolean} True if piece belongs to opponent
   */
  const isOpponentPiece = (piece, playerColor) => {
    if (!piece) return false;
    return playerColor === 'white' ? isBlackPiece(piece) : isWhitePiece(piece);
  };

  /**
   * Check if a piece belongs to the same player
   * @param {string|null} piece - The piece to check
   * @param {string} playerColor - Current player color ('white' or 'black')
   * @returns {boolean} True if piece belongs to same player
   */
  const isSameColorPiece = (piece, playerColor) => {
    if (!piece) return false;
    return playerColor === 'white' ? isWhitePiece(piece) : isBlackPiece(piece);
  };

  // ============================================================================
  // CHESS PIECE MOVEMENT LOGIC
  // ============================================================================

  /**
   * Generate all valid moves for a specific piece at given position
   * @param {number} row - Current row of the piece
   * @param {number} col - Current column of the piece
   * @param {Array} boardState - Current board state
   * @returns {Array} Array of valid move coordinates [[row, col], ...]
   */
  const generatePieceMoves = (row, col, boardState) => {
    const piece = boardState[row][col];
    if (!piece) return []; // No piece at this position

    const color = isWhitePiece(piece) ? 'white' : 'black';
    const moves = [];
    const pieceType = piece.toLowerCase(); // Get piece type regardless of color

    /**
     * Helper function to add a move if valid
     * @param {number} r - Target row
     * @param {number} c - Target column
     * @returns {boolean} True if can continue in this direction, false if blocked
     */
    const addMove = (r, c) => {
      if (!isValidPosition(r, c)) return false; // Out of bounds
      
      const target = boardState[r][c];
      if (!target) {
        // Empty square - valid move, can continue in this direction
        moves.push([r, c]);
        return true;
      } else if (isOpponentPiece(target, color)) {
        // Opponent piece - valid capture, but can't continue past it
        moves.push([r, c]);
        return false;
      }
      // Same color piece - blocked, can't move here or continue
      return false;
    };

    // Generate moves based on piece type
    switch (pieceType) {
      case 'p': // Pawn movement logic
        const direction = color === 'white' ? -1 : 1; // White pawns move up (-1), black down (+1)
        const startRow = color === 'white' ? 6 : 1;   // Starting row for pawns

        // Forward movement (one or two squares from starting position)
        if (!boardState[row + direction]?.[col]) { // Check if one square ahead is empty
          moves.push([row + direction, col]);
          
          // Two-square move from starting position
          if (row === startRow && !boardState[row + 2 * direction]?.[col]) {
            moves.push([row + 2 * direction, col]);
          }
        }

        // Diagonal captures (pawns capture diagonally)
        [-1, 1].forEach(dc => {
          const newRow = row + direction;
          const newCol = col + dc;
          if (isValidPosition(newRow, newCol) && isOpponentPiece(boardState[newRow][newCol], color)) {
            moves.push([newRow, newCol]);
          }
        });
        break;

      case 'r': // Rook movement (horizontal and vertical lines)
        [[0, 1], [0, -1], [1, 0], [-1, 0]].forEach(([dr, dc]) => {
          // Move in each direction until blocked or reach edge
          for (let i = 1; i < 8; i++) {
            if (!addMove(row + dr * i, col + dc * i)) break;
          }
        });
        break;

      case 'n': // Knight movement (L-shaped moves)
        [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]].forEach(([dr, dc]) => {
          addMove(row + dr, col + dc);
        });
        break;

      case 'b': // Bishop movement (diagonal lines)
        [[-1, -1], [-1, 1], [1, -1], [1, 1]].forEach(([dr, dc]) => {
          // Move diagonally until blocked or reach edge
          for (let i = 1; i < 8; i++) {
            if (!addMove(row + dr * i, col + dc * i)) break;
          }
        });
        break;

      case 'q': // Queen movement (combines rook and bishop)
        [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]].forEach(([dr, dc]) => {
          // Move in all 8 directions until blocked or reach edge
          for (let i = 1; i < 8; i++) {
            if (!addMove(row + dr * i, col + dc * i)) break;
          }
        });
        break;

      case 'k': // King movement (one square in any direction)
        [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]].forEach(([dr, dc]) => {
          addMove(row + dr, col + dc);
        });
        break;
    }

    return moves;
  };

  /**
   * Get all possible moves for a player (used by AI for decision making)
   * @param {string} color - Player color ('white' or 'black')
   * @param {Array} boardState - Current board state
   * @returns {Array} Array of move objects with 'from' and 'to' properties
   */
  const getAllValidMoves = (color, boardState) => {
    const moves = [];
    
    // Iterate through entire board
    for (let row = 0; row < 8; row++) {
      for (let col = 0; col < 8; col++) {
        const piece = boardState[row][col];
        
        // If piece belongs to current player, get its moves
        if (piece && isSameColorPiece(piece, color)) {
          const pieceMoves = generatePieceMoves(row, col, boardState);
          pieceMoves.forEach(([toRow, toCol]) => {
            moves.push({ from: [row, col], to: [toRow, toCol] });
          });
        }
      }
    }
    
    return moves;
  };

  // ============================================================================
  // GAME STATE EVALUATION AND WIN CONDITIONS
  // ============================================================================

  /**
   * Check if a king of specified color has been captured
   * @param {string} color - Color to check ('white' or 'black')
   * @param {Array} boardState - Current board state
   * @returns {boolean} True if king is captured (not found on board)
   */
  const isKingCaptured = (color, boardState) => {
    const king = color === 'white' ? 'K' : 'k';
    
    // Search entire board for the king
    for (let row = 0; row < 8; row++) {
      for (let col = 0; col < 8; col++) {
        if (boardState[row][col] === king) {
          return false; // King found, not captured
        }
      }
    }
    
    return true; // King not found, has been captured
  };

  /**
   * Evaluate board position for AI decision making
   * Positive scores favor black (AI), negative scores favor white (human)
   * @param {Array} boardState - Board state to evaluate
   * @returns {number} Evaluation score
   */
  const evaluateBoard = (boardState) => {
    // Piece values for evaluation (standard chess piece values)
    const pieceValues = { 
      p: 1,   // Pawn
      n: 3,   // Knight
      b: 3,   // Bishop
      r: 5,   // Rook
      q: 9,   // Queen
      k: 100  // King (high value to prioritize king safety)
    };
    
    let score = 0;
    let whiteKingExists = false;
    let blackKingExists = false;

    // Calculate material balance
    for (let row = 0; row < 8; row++) {
      for (let col = 0; col < 8; col++) {
        const piece = boardState[row][col];
        if (piece) {
          const value = pieceValues[piece.toLowerCase()];
          
          // Track king existence
          if (piece === 'K') whiteKingExists = true;
          if (piece === 'k') blackKingExists = true;
          
          // Add to score (negative for white pieces, positive for black pieces)
          score += isWhitePiece(piece) ? -value : value;
        }
      }
    }

    // Massive bonuses for capturing the opponent's king
    if (!whiteKingExists) score += 10000; // AI wins
    if (!blackKingExists) score -= 10000; // Human wins

    return score;
  };

  // ============================================================================
  // AI DECISION MAKING (MINIMAX ALGORITHM)
  // ============================================================================

  /**
   * Minimax algorithm with alpha-beta pruning for AI move selection
   * @param {Array} boardState - Current board state
   * @param {number} depth - Search depth (how many moves ahead to look)
   * @param {boolean} isMaximizing - True if maximizing player's turn (AI/black)
   * @param {number} alpha - Alpha value for pruning
   * @param {number} beta - Beta value for pruning
   * @returns {Object} Object with 'score' and optionally 'move'
   */
  const minimax = (boardState, depth, isMaximizing, alpha, beta) => {
    // Base case: reached maximum depth, evaluate position
    if (depth === 0) {
      return { score: evaluateBoard(boardState) };
    }

    const color = isMaximizing ? 'black' : 'white';
    const moves = getAllValidMoves(color, boardState);

    // No moves available (shouldn't happen in our simplified game)
    if (moves.length === 0) {
      return { score: 0 };
    }

    let bestMove = null;
    let bestScore = isMaximizing ? -Infinity : Infinity;

    // Try each possible move
    for (const move of moves) {
      const [fromRow, fromCol] = move.from;
      const [toRow, toCol] = move.to;

      // Create new board state with this move applied
      const newBoard = boardState.map(row => [...row]);
      newBoard[toRow][toCol] = newBoard[fromRow][fromCol]; // Move piece
      newBoard[fromRow][fromCol] = null; // Clear original position

      // Recursively evaluate this position
      const result = minimax(newBoard, depth - 1, !isMaximizing, alpha, beta);

      // Update best move based on whether we're maximizing or minimizing
      if (isMaximizing) {
        if (result.score > bestScore) {
          bestScore = result.score;
          bestMove = move;
        }
        alpha = Math.max(alpha, result.score);
      } else {
        if (result.score < bestScore) {
          bestScore = result.score;
          bestMove = move;
        }
        beta = Math.min(beta, result.score);
      }

      // Alpha-beta pruning: if beta <= alpha, we can stop searching
      if (beta <= alpha) break;
    }

    return { score: bestScore, move: bestMove };
  };

  // ============================================================================
  // AI MOVE EXECUTION
  // ============================================================================

  /**
   * Execute AI move using minimax algorithm
   * Uses useCallback to prevent unnecessary re-renders
   */
  const makeAIMove = useCallback(() => {
    // Only make move if it's AI's turn and game is still playing
    if (currentPlayer !== 'black' || gameStatus !== 'playing') return;

    setIsThinking(true); // Show thinking indicator

    // Add slight delay for better UX (shows AI is "thinking")
    setTimeout(() => {
      // Get best move using minimax with depth 3 (looks 3 moves ahead)
      const result = minimax(board, 3, true, -Infinity, Infinity);

      if (result.move) {
        const [fromRow, fromCol] = result.move.from;
        const [toRow, toCol] = result.move.to;

        // Apply the AI's move to the board
        const newBoard = board.map(row => [...row]);
        newBoard[toRow][toCol] = newBoard[fromRow][fromCol];
        newBoard[fromRow][fromCol] = null;

        setBoard(newBoard);
        setCurrentPlayer('white'); // Switch back to human player

        // Check for game end conditions
        if (isKingCaptured('white', newBoard)) {
          setGameStatus('black-wins');
        } else if (isKingCaptured('black', newBoard)) {
          setGameStatus('white-wins');
        }
      }

      setIsThinking(false); // Hide thinking indicator
    }, 500); // 500ms delay for visual effect
  }, [board, currentPlayer, gameStatus]);

  // ============================================================================
  // REACT EFFECTS AND EVENT HANDLERS
  // ============================================================================

  /**
   * Effect to trigger AI move when it becomes AI's turn
   * Runs whenever currentPlayer or gameStatus changes
   */
  useEffect(() => {
    if (currentPlayer === 'black' && gameStatus === 'playing') {
      makeAIMove();
    }
  }, [currentPlayer, gameStatus, makeAIMove]);

  /**
   * Handle click on a chess board square
   * Manages piece selection, move validation, and move execution for human player
   * @param {number} row - Clicked row
   * @param {number} col - Clicked column
   */
  const handleSquareClick = (row, col) => {
    // Ignore clicks if not human's turn, game over, or AI is thinking
    if (currentPlayer !== 'white' || gameStatus !== 'playing' || isThinking) return;

    const piece = board[row][col];

    if (selectedSquare) {
      // A piece is already selected - try to move it
      const [selectedRow, selectedCol] = selectedSquare;
      const isValidMove = validMoves.some(([r, c]) => r === row && c === col);

      if (isValidMove) {
        // Valid move - execute it
        const newBoard = board.map(row => [...row]);
        newBoard[row][col] = newBoard[selectedRow][selectedCol];
        newBoard[selectedRow][selectedCol] = null;

        setBoard(newBoard);
        setSelectedSquare(null);  // Clear selection
        setValidMoves([]);        // Clear valid moves

        // Check for game end conditions
        if (isKingCaptured('black', newBoard)) {
          setGameStatus('white-wins');
          return;
        } else if (isKingCaptured('white', newBoard)) {
          setGameStatus('black-wins');
          return;
        }

        // Switch to AI's turn
        setCurrentPlayer('black');
      } else {
        // Invalid move - clear selection
        setSelectedSquare(null);
        setValidMoves([]);
      }
    } else if (piece && isWhitePiece(piece)) {
      // No piece selected and clicked on white piece - select it
      const moves = generatePieceMoves(row, col, board);
      setSelectedSquare([row, col]);
      setValidMoves(moves);
    }
    // If clicked on empty square or black piece with no selection, do nothing
  };

  /**
   * Reset the game to initial state
   */
  const resetGame = () => {
    setBoard(initialBoard);
    setCurrentPlayer('white');
    setSelectedSquare(null);
    setValidMoves([]);
    setGameStatus('playing');
    setIsThinking(false);
  };

  // ============================================================================
  // VISUAL STYLING FUNCTIONS
  // ============================================================================

  /**
   * Get CSS classes for a chess board square based on its state
   * @param {number} row - Square row
   * @param {number} col - Square column
   * @returns {string} CSS class string
   */
  const getSquareClass = (row, col) => {
    // Base color: alternating light and dark squares
    let className = (row + col) % 2 === 0 ? 'bg-amber-100' : 'bg-amber-700';

    // Highlight selected square
    if (selectedSquare && selectedSquare[0] === row && selectedSquare[1] === col) {
      className += ' ring-4 ring-green-500 bg-green-300';
    } 
    // Highlight valid move squares
    else if (validMoves.some(([r, c]) => r === row && c === col)) {
      className += ' bg-blue-300';
    }

    return className;
  };

  /**
   * Get inline styles for piece rendering (white pieces need shadow for visibility)
   * @param {string} piece - The piece character
   * @returns {Object} Style object
   */
  const getPieceStyle = (piece) => {
    // White pieces need text shadow to be visible on light squares
    if (isWhitePiece(piece)) {
      return { color: '#ffffff', textShadow: '1px 1px 2px #000000' };
    }
    return {}; // Black pieces are fine with default styling
  };

  // ============================================================================
  // RENDER THE CHESS GAME UI
  // ============================================================================

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-purple-600 to-blue-600 p-4">
      <div className="bg-white rounded-xl shadow-2xl p-8 max-w-2xl">
        
        {/* Game Header with Title and Status */}
        <div className="text-center mb-6">
          <h1 className="text-3xl font-bold text-gray-800 mb-2">Chess Game</h1>
          <div className="text-xl font-semibold text-gray-600">
            {gameStatus === 'playing' ? (
              <>
                {/* Show current turn or AI thinking status */}
                {currentPlayer === 'white' ? 'Your Turn' : 'AI Thinking...'}
                {isThinking && <span className="ml-2 animate-spin">🤔</span>}
              </>
            ) : gameStatus === 'black-wins' ? (
              '🤖 AI Wins! King Captured!'
            ) : gameStatus === 'white-wins' ? (
              '🎉 You Win! King Captured!'
            ) : (
              "It's a Draw!"
            )}
          </div>
        </div>

        {/* Chess Board Grid */}
        <div className="grid grid-cols-8 gap-0 border-4 border-amber-900 rounded-lg overflow-hidden mb-6 mx-auto w-fit">
          {board.map((row, rowIndex) =>
            row.map((piece, colIndex) => (
              <div
                key={`${rowIndex}-${colIndex}`}
                className={`w-16 h-16 flex items-center justify-center text-4xl cursor-pointer hover:scale-105 transition-transform ${getSquareClass(rowIndex, colIndex)}`}
                onClick={() => handleSquareClick(rowIndex, colIndex)}
              >
                {/* Render piece if present */}
                {piece && (
                  <span style={getPieceStyle(piece)}>
                    {pieces[piece]}
                  </span>
                )}
              </div>
            ))
          )}
        </div>

        {/* New Game Button (only shown when game is over) */}
        {gameStatus !== 'playing' && (
          <div className="text-center">
            <button
              onClick={resetGame}
              className="bg-blue-500 hover:bg-blue-600 text-white font-bold py-3 px-6 rounded-lg transition-colors"
            >
              New Game
            </button>
          </div>
        )}

        {/* Game Instructions */}
        <div className="text-center text-sm text-gray-600 mt-4">
          <p>You play as White (bottom). Click a piece to select, then click a highlighted square to move.</p>
          <p className="mt-1 font-semibold text-red-600">Game ends only when a King is captured!</p>
        </div>
      </div>
    </div>
  );
};

export default ChessGame;