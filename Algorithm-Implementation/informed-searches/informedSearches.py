from collections import defaultdict
import heapq

class InformedGraph:
    def __init__(self):
        self.graph = defaultdict(list)  # graph[node] = [(neighbor, cost), ...]
        self.heuristics = {}  # heuristics[node] = h(n)
        self.and_or_graph = defaultdict(list)  # Used for AO* Search

    # Add an undirected edge with a cost
    def add_edge(self, u, v, cost=1):
        self.graph[u].append((v, cost))
        self.graph[v].append((u, cost))

    # Set heuristic value for a node
    def set_heuristic(self, node, value):
        self.heuristics[node] = value

    # Add AND-OR graph edges (parent -> [(child, is_and)])
    def add_and_or_edge(self, parent, child, is_and=True):
        self.and_or_graph[parent].append((child, is_and))

    # Display the graph
    def iterate(self):
        for node in self.graph:
            print(f"{node} → {self.graph[node]}")

    # ------------------------ Best First Search ------------------------
    def best_first_search(self, start, goal):
        visited = set()
        pq = [(self.heuristics.get(start, float('inf')), start)]  # (heuristic, node)

        print("Best First Search Path: ", end='')
        while pq:
            _, current = heapq.heappop(pq)
            if current == goal:
                print(current)
                return

            visited.add(current)
            print(current, end=' → ')

            for neighbor, _ in self.graph.get(current, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (self.heuristics.get(neighbor, float('inf')), neighbor))

        print("Goal not reachable")             
            
        

    # ------------------------ A* Search ------------------------
    def a_star_search(self, start, goal):
        open_set = [(self.heuristics.get(start, float('inf')), 0, start)]  # (f = g + h, g, node)
        came_from = {}
        g_cost = {start: 0}

        while open_set:
            _, g, current = heapq.heappop(open_set)

            if current == goal:
                path = self.reconstruct_path(came_from, current)
                print("A* Search Path: ", " → ".join(path))
                return

            for neighbor, cost in self.graph.get(current, []):
                new_g = g + cost
                if neighbor not in g_cost or new_g < g_cost[neighbor]:
                    g_cost[neighbor] = new_g
                    f = new_g + self.heuristics.get(neighbor, float('inf'))
                    heapq.heappush(open_set, (f, new_g, neighbor))
                    came_from[neighbor] = current

        print("Goal not reachable")

    # ------------------------ AO* Search ------------------------
    def ao_star_search(self, start, goal):
        # AO* works with AND-OR graphs
        open_set = [(0, start)]  # (cost, node)
        best_cost = {start: 0}
        node_parent = {start: None}

        while open_set:
            cost, current = heapq.heappop(open_set)

            # If we reach the goal, trace the path
            if current == goal:
                path = self.reconstruct_ao_path(node_parent, current)
                print("AO* Search Path: ", " → ".join(path))
                return

            # Explore neighbors from AND-OR graph
            for neighbor, is_and in self.and_or_graph[current]:
                # If it's an AND node, all children must be valid
                if is_and:
                    if neighbor not in best_cost or cost + 1 < best_cost[neighbor]:
                        best_cost[neighbor] = cost + 1
                        heapq.heappush(open_set, (cost + 1, neighbor))
                        node_parent[neighbor] = current
                else:
                    # If it's an OR node, any valid child is sufficient
                    if neighbor not in best_cost or cost + 1 < best_cost[neighbor]:
                        best_cost[neighbor] = cost + 1
                        heapq.heappush(open_set, (cost + 1, neighbor))
                        node_parent[neighbor] = current

        print("Goal not reachable")

    # ------------------------ Path Reconstruction ------------------------
    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    # ------------------------ AO* Path Reconstruction ------------------------
    def reconstruct_ao_path(self, node_parent, current):
        path = [current]
        while current in node_parent and node_parent[current] is not None:
            current = node_parent[current]
            path.append(current)
        path.reverse()
        return path


# ------------------------ Example Usage ------------------------

if __name__ == "__main__":
    g = InformedGraph()
    g.add_edge('A', 'B', 1)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('C', 'D', 1)
    g.add_edge('B', 'E', 6)
    g.add_edge('D', 'E', 1)

    g.set_heuristic('A', 7)
    g.set_heuristic('B', 6)
    g.set_heuristic('C', 2)
    g.set_heuristic('D', 1)
    g.set_heuristic('E', 0)

    # Set up AND-OR graph for AO* Search (with is_and = True or False)
    g.add_and_or_edge('A', 'B', is_and=True)
    g.add_and_or_edge('A', 'C', is_and=False)
    g.add_and_or_edge('B', 'D', is_and=False)
    g.add_and_or_edge('C', 'D', is_and=True)
    g.add_and_or_edge('B', 'E', is_and=True)
    g.add_and_or_edge('D', 'E', is_and=False)

    print("\nGraph:")
    g.iterate()

    print("\n--- Best First Search ---")
    g.best_first_search('A', 'E')

    print("\n--- A* Search ---")
    g.a_star_search('A', 'E')

    print("\n--- AO* Search ---")
    g.ao_star_search('A', 'E')
