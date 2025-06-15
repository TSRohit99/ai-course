from collections import defaultdict , deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(set)
    
    #add edges (for undirected)
    def add_edges(self,u,v):
        self.graph[u].add(v)
        self.graph[v].add(u)

    def iterate(self):
        for node in self.graph.keys():
            print(f"{node} -> : {self.graph[node]}")
    
    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=' ')
            for neighbor in sorted(self.graph.get(vertex, [])):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

    def dfs(self, node, visited = None):
        if visited is None:
            visited = set()
        visited.add(node)    
        # print(node, end = ' ')

        for neighbor in self.graph.get(node,[]):
            if neighbor not in visited:
                self.dfs(neighbor, visited)
                print(neighbor, end=' ' )

    def depth_limited_dfs(self, start, target, limit):
        if start == target:
            print(f"Target Found!")
            return True
        if limit <= 0:
            return False
        
        for neighbor in self.graph.get(start, []):
            if self.depth_limited_dfs(neighbor, target, limit - 1):
                return True
            
        return False
    
    def ids(self, start, target, max_depth_limit):
        for depth in range(max_depth_limit + 1):
            print(f"Depth Level : {depth}")
            isFound = self.depth_limited_dfs(start,target,depth)
            if isFound:
                print(f"Target Found  {depth} depth")
                return True
            print(f"Not found in level {depth}")
       
        print("Target not found!")  
        return False
    


    def bds(self, start, goal):
        if start == goal:
            return [start]
        
        frontier_start = deque([start]) #Starting Point (Appends in each iteration)
        frontier_goal = deque([goal]) #  Goal point starting

        visited_by_start = {start : None} # initalizer for both visited so while constructing the path itll be easier to check
        visited_by_goal = {goal : None}

        while frontier_start and frontier_goal:
            result = self.forward_frontier(frontier_start, visited_by_start ,visited_by_goal)
            if result:
               return self.build_path(result, visited_by_start, visited_by_goal)

            result = self.forward_frontier(frontier_goal, visited_by_goal ,visited_by_start)   
            if result:
              return  self.build_path(result, visited_by_start, visited_by_goal) 
            
        return "No matched entires!"  

    def forward_frontier(self, frontier , visited_by_self , visited_by_other):
        current = frontier.popleft()  
        
        for neighbor in self.graph.get(current, []):
            if neighbor not in visited_by_self:
                visited_by_self[neighbor] = current
                frontier.append(current)

            if neighbor in visited_by_other: 
                return neighbor # meeting point from both side
        return None  
    
    def build_path(self, meeting_point, visited_by_start, visisted_by_goal):
        start_path = []
        node = meeting_point
        while node:
            start_path.append(node)
            node = visited_by_start[node]
        start_path.reverse()

        goal_path = []
        node = visisted_by_goal[meeting_point]
        while node:
            goal_path.append(node)
            node = visisted_by_goal[node]     
        
        return start_path + goal_path
        


    
         



g = Graph()
g.add_edges(3,6)
g.add_edges(6,0)
g.add_edges(6,4)
g.add_edges(3,9)
g.add_edges(9,5)
g.add_edges(9,7)

g.iterate()
print ("BFS :",g.bfs(3))
print ("DFS :",g.dfs(3))
print ("DLS :")
if not g.depth_limited_dfs(3,4,0):
    print("Target not Found!")
print ("Iterative Deeping Search :")
g.ids(3,7,2)
print("Bidirectional Search : ", g.bds(3,7))



