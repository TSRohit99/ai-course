# Local Search Algorithms Implementation 🏔️

A comprehensive Python implementation of local search algorithms that focus on finding good solutions efficiently without exploring the entire search space.

## 📋 Table of Contents
- [Algorithms Implemented](#algorithms-implemented)
- [How Algorithms Work](#how-algorithms-work)
- [Applications](#applications)
- [Complexity Analysis](#complexity-analysis)
- [Input & Output Examples](#input--output-examples)
- [Usage](#usage)

## 🚀 Algorithms Implemented

- **Hill Climbing** 🏔️
- **Beam Search** 🔦

## 🧠 How Algorithms Work

### 🏔️ Hill Climbing
A greedy local search that moves to the best neighboring state. Continues until reaching a local optimum where no neighbor is better than the current state. Simple but can get stuck in local maxima.

### 🔦 Beam Search
Systematic search that maintains a fixed number of best nodes (beam width) at each level. Combines breadth-first exploration with heuristic pruning to balance completeness and efficiency.

## 🎯 Applications

### 🏔️ Hill Climbing Applications
- **Optimization Problems** - function maximization/minimization
- **Machine Learning** - gradient ascent/descent
- **Scheduling** - task assignment optimization
- **Network Configuration** - parameter tuning
- **Game AI** - position evaluation and improvement
- **Resource Allocation** - local optimization

### 🔦 Beam Search Applications
- **Natural Language Processing** - speech recognition, translation
- **Bioinformatics** - sequence alignment
- **Scheduling Problems** - job shop scheduling
- **Route Planning** - approximate pathfinding
- **Constraint Satisfaction** - partial solution exploration
- **Image Recognition** - feature matching

## ⚡ Complexity Analysis

| Algorithm | Time Complexity | Space Complexity | Optimal? | Complete? | Memory Usage |
|-----------|----------------|------------------|----------|-----------|--------------|
| **Hill Climbing** 🏔️ | O(k × b) | O(1) | ❌ No | ❌ No | Very Low |
| **Beam Search** 🔦 | O(b^d × log(β)) | O(β × d) | ❌ No | ❌ No | Moderate |

**Legend:**
- `k` = Number of steps to local optimum
- `b` = Branching factor
- `d` = Depth of search
- `β` = Beam width
- `log(β)` = Sorting cost for beam selection

**Characteristics:**
- **Hill Climbing**: Fast, memory-efficient, but incomplete
- **Beam Search**: More thorough than hill climbing, tunable exploration

## 📸 Input & Output Examples

### 🔧 Input Graph Structure
```
Graph with Heuristic Values:
Node 0 → [1, 2, 3] (h: 6)
Node 1 → [4]       (h: 5)
Node 2 → []        (h: 4)
Node 3 → [5]       (h: 3)
Node 4 → []        (h: 3)
Node 5 → [8]       (h: 2)
Node 8 → []        (h: 0) ← Goal
```

### 📊 Sample Outputs

<img width="1495" alt="localS" src="https://github.com/user-attachments/assets/1f6b9b9f-1a74-4b4b-96bd-8aa91262ebd2" />


## 🛠️ Usage

### Basic Setup
```python
# Create search algorithms instance
search = SearchAlgorithms()

# Define graph structure
search.graph = {
    0: [1, 2, 3],
    1: [4],
    2: [],
    3: [5],
    4: [],
    5: [8],
    8: [],
}

# Set heuristic values (lower is better - distance to goal)
search.heuristics = {
    0: 6,  # Start node
    1: 5,
    2: 4,
    3: 3,
    4: 3,
    5: 2,
    8: 0,  # Goal node
}
```

### Running Algorithms
```python
# Hill Climbing Search
result = search.hill_climbing(start=0, goal=8)
if result:
    print(f"Hill Climbing Path: {result}")

# Beam Search with different beam widths
result = search.beam_search(start=0, goal=8, beam_width=2)
if result:
    print(f"Beam Search Path: {result}")

# Try different beam widths for comparison
search.beam_search(start=0, goal=8, beam_width=1)  # Greedy
search.beam_search(start=0, goal=8, beam_width=3)  # Broader search
```

## 🔍 Algorithm Comparison

| Feature | Hill Climbing 🏔️ | Beam Search 🔦 |
|---------|------------------|----------------|
| **Search Strategy** | Local greedy | Level-wise with pruning |
| **Memory Usage** | Constant | Linear in beam width |
| **Solution Quality** | Local optimum | Better exploration |
| **Speed** | Very Fast | Moderate |
| **Completeness** | No | No |
| **Tunability** | None | Beam width parameter |

## 🏗️ Implementation Features

### Core Components
- ✅ **Graph Representation** - adjacency list structure
- ✅ **Heuristic Management** - node evaluation system
- ✅ **Path Tracking** - complete solution reconstruction
- ✅ **Neighbor Exploration** - systematic state expansion
- ✅ **Local Optimization** - greedy improvement strategy

### Advanced Features
- 🔧 **Flexible Beam Width** - tunable exploration breadth
- 📊 **Detailed Logging** - step-by-step search visualization
- 🎯 **Heuristic Sorting** - efficient node ranking
- 🔄 **Level-wise Processing** - systematic exploration
- ⚡ **Early Termination** - goal detection optimization

## 📚 Requirements

```python
# No external dependencies required!
# Built with Python's standard library
```

Pure Python implementation - no external dependencies! 🎉

## 🎯 Key Advantages & Limitations

### 🏔️ Hill Climbing
**Advantages:**
- **Memory Efficient**: O(1) space complexity
- **Fast Execution**: Quick convergence to local optimum
- **Simple Implementation**: Easy to understand and modify
- **Low Overhead**: Minimal computational requirements

**Limitations:**
- **Local Optima**: Gets stuck in local peaks
- **Incomplete**: May not find existing solutions
- **No Backtracking**: Cannot recover from bad choices
- **Plateau Problems**: Struggles with flat landscapes

### 🔦 Beam Search
**Advantages:**
- **Better Exploration**: Maintains multiple candidates
- **Tunable Performance**: Adjustable beam width
- **Systematic Search**: Level-wise exploration
- **Balanced Approach**: Compromise between BFS and greedy

**Limitations:**
- **Memory Requirements**: Linear space in beam width
- **Still Incomplete**: Can miss optimal solutions
- **Parameter Sensitivity**: Performance depends on beam width
- **No Optimality Guarantee**: Heuristic-guided approximation

## 🚨 Important Notes

### Parameter Tuning
- **Beam Width**: Larger values → better solutions, more memory
- **Heuristic Quality**: Better heuristics → more efficient search
- **Graph Structure**: Dense graphs benefit more from beam search

### When to Use
- **Hill Climbing**: When memory is limited and quick approximation is needed
- **Beam Search**: When better solution quality is worth extra memory cost

### Common Pitfalls
- **Local Optima**: Consider random restarts for hill climbing
- **Beam Width**: Too small → poor solutions, too large → excessive memory
- **Heuristic Design**: Poor heuristics can mislead both algorithms

## 🔄 Extensions & Variations

### Hill Climbing Variants
- **Random Restart**: Multiple runs from different starting points
- **Stochastic**: Probabilistic neighbor selection
- **First-Choice**: Accept first improving neighbor

### Beam Search Variants
- **Local Beam Search**: Nodes can share information
- **Stochastic Beam Search**: Probabilistic selection within beam
- **Adaptive Beam**: Dynamic beam width adjustment

---

*Efficiently navigate complex search spaces with local optimization strategies!* 🗺️⚡