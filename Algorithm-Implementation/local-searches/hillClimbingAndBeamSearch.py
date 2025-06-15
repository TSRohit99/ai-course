class SearchAlgorithms:
    def __init__(self):
        self.graph = {}
        self.heuristics = {}

    # ------------------------ Hill Climbing ------------------------
    def hill_climbing(self, start, goal):
        current = start
        path = [current]

        while True:
            neighbors = self.get_neighbors(current)
            if not neighbors:
                print("Hill Climbing: No neighbors to explore.")
                return None

            next_node = min(neighbors, key=lambda neighbor: self.get_heuristic(neighbor, goal))

            if self.get_heuristic(next_node, goal) >= self.get_heuristic(current, goal):
                print("Hill Climbing: Reached local optimum.")
                return path

            current = next_node
            path.append(current)

            if current == goal:
                return path

    # ------------------------ Beam Search (Proper Path Tracking) ------------------------
    def beam_search(self, start, goal, beam_width=2):
        # Initialize the starting level with the start node and its path
        current_level = [(start, [start])]
        
        print(f"--- Beam Search Started ---")
        print(f"Start Node: {start}, Goal Node: {goal}")
        print(f"Beam Width: {beam_width}\n")
        
        # Main loop to explore the graph
        while current_level:
            next_level = []
            print(f"Current Level: {[(node, path) for node, path in current_level]}")
            
            for node, path in current_level:
                # If the goal is found, return the path
                if node == goal:
                    print(f"Goal found! Path: {path}")
                    return path
                
                # Get the neighbors of the current node
                neighbors = self.get_neighbors(node)
                print(f"Exploring node {node} with path {path}. Neighbors: {neighbors}")
                
                # For each neighbor, create a new path and add it to the next level
                for neighbor in neighbors:
                    new_path = path + [neighbor]
                    next_level.append((neighbor, new_path))
            
            # If no new level to explore, exit the search
            if not next_level:
                print("No more nodes to explore. Search terminated.")
                break
            
            # Sort the next level by heuristic values (distance to the goal)
            next_level.sort(key=lambda x: self.get_heuristic(x[0], goal))
            
            # Display the sorted next level and its heuristic values
            print(f"Sorted Next Level by Heuristic (Distance to Goal):")
            for node, path in next_level:
                print(f"Node {node} with path {path}, Heuristic: {self.get_heuristic(node, goal)}")
            
            # Keep only the top 'beam_width' nodes in the next level
            current_level = next_level[:beam_width]
            print(f"Selected Top {beam_width} Nodes for Next Level: {[(node, path) for node, path in current_level]}\n")
        
        # If the goal was not found after exploring all levels
        print("Beam Search: No solution found.")
        return None

        

    # ------------------------ Utility Functions ------------------------
    def get_neighbors(self, node):
        return self.graph.get(node, [])

    def get_heuristic(self, node, goal):
        return self.heuristics.get(node, float('inf'))

    # ------------------------ Example Usage ------------------------
    def example_usage(self):
        # Graph structure
        self.graph = {
            0: [1, 2, 3],
            1: [4],
            2: [],
            3: [5],
            4: [],
            5: [8],
            8: [],
        }

        # Heuristic values (lower is better)
        self.heuristics = {
            0: 6,
            1: 5,
            2: 4,
            3: 3,
            4: 3,
            5: 2,
            8: 0,
        }

        print("\n--- Hill Climbing ---")
        result = self.hill_climbing(0, 8)
        if result:
            print(f"Hill Climbing Result: {result}")
        else:
            print("Hill Climbing failed.")

        print("\n--- Beam Search ---")
        result = self.beam_search(0, 8, beam_width=2)
        if result:
            print(f"Beam Search Result: {result}")
        else:
            print("Beam Search failed.")


# ------------------------ Run the Example ------------------------
if __name__ == "__main__":
    search = SearchAlgorithms()
    search.example_usage()
