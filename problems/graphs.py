import collections

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# https://leetcode.com/problems/keys-and-rooms/
def can_visit_all_rooms(rooms: list[list[int]]) -> bool:
        visited = set()
        
        def _dfs(i):
            visited.add(i)
            keys = rooms[i]
            for key in keys:
                if key not in visited:
                    _dfs(key)
        _dfs(0)

        return len(visited) == len(rooms)

# https://leetcode.com/problems/number-of-provinces
def find_circle_num(is_connected: list[list[int]]) -> int:
    n = len(is_connected)
    num = 0
    visited = set()

    def _dfs(i):
        visited.add(i)
        for j in range(n):
            if j not in visited and is_connected[i][j]:
                _dfs(j)
    for i in range(n):
        if i not in visited:
            _dfs(i)
            num +=1
    return num

# https://leetcode.com/problems/number-of-islands/
def numIslands(grid: list[list[str]]) -> int:
    visited = set()
    # dfs on every point that hasn't been visited
    rows, cols = len(grid), len(grid[0])
    num_islands = 0
    # def _dfs(x,y):
    #     visited.add((x,y))
    #     dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    #     for dx,dy in dirs:
    #         if (x+dx,y+dy) not in visited and x+dx in range(rows) and y+dy in range(cols) and grid[x+dx][y+dy] == "1":
    #             _dfs(x+dx,y+dy)

    def _bfs(i,j):
        q = collections.deque()
        visited.add((i,j))
        q.append((i,j))
        while q:
            x,y = q.popleft()
            dirs = [(0,1),(0,-1),(1,0),(-1,0)]
            for dx, dy in dirs:
                if (x+dx,y+dy) not in visited and x+dx in range(rows) and y+dy in range(cols) and grid[x+dx][y+dy] == "1":
                    visited.add((x+dx,y+dy))
                    q.append((x+dx,y+dy))

    for i in range(rows):
        for j in range(cols):
            if (i,j) not in visited and grid[i][j] == "1":
                # _dfs(i,j)
                _bfs(i,j)
                num_islands += 1
    return num_islands

# https://leetcode.com/problems/clone-graph/
def cloneGraph(self, node: 'Node') -> 'Node':
    if not node:
        return None
    #         new_nodes = [None]*101
    #         q = collections.deque()
    #         q.append(node)

    #         while q:
    #             n = q.popleft()
    #             if not new_nodes[n.val]:
    #                 new_nodes[n.val] = Node(n.val)

    #             n_neighbors = []
    #             for neighbor in n.neighbors:
    #                 n_neighbors.append(neighbor.val)
    #                 if not new_nodes[neighbor.val]:
    #                     new_nodes[neighbor.val] = Node(neighbor.val)
    #                     q.append(neighbor)
    #             new_nodes[n.val].neighbors = [new_nodes[i] for i in n_neighbors]

    #         return new_nodes[node.val]

    old_to_new = {}

    def clone(node):
        if node in old_to_new:
            return old_to_new[node]

        copy = Node(node.val)
        old_to_new[node] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(clone(neighbor))
        return copy

    clone(node)
    return old_to_new[node]

# https://leetcode.com/problems/course-schedule/
def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
    has_cycle = False
    visited = set()
    graph = collections.defaultdict(list)
    for edge in prerequisites:
        graph[edge[0]].append(edge[1])

    def dfs(node, v):
        nonlocal has_cycle
        if node in visited:
            return
        if node in v:
            has_cycle = True
            return

        v.add(node)
        for nei in graph[node]:
            dfs(nei, v)
        v.remove(node)
        visited.add(node)

    for node in graph.copy():
        if node not in visited:
            dfs(node, set())

    return not has_cycle

# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#     def countComponents(self, n: int, edges: list[list[int]]) -> int:
#         num_components = 0
#         self.visited = [False] * n


#         self.graph = {x: [] for x in range(n)}

#         for edge in edges:
#             self.graph[edge[0]].append(edge[1])
#             self.graph[edge[1]].append(edge[0])
#         print(self.graph)

#         for node in self.graph:
#             if not self.visited[node]:
#                 self.dfs(node)
#                 num_components += 1

#         return num_components

#     def dfs(self, node):
#         self.visited[node] = True
#         for neighbor in self.graph[node]:
#             if not self.visited[neighbor]:
#                 self.dfs(neighbor)

def countComponents(self, n: int, edges: list[list[int]]) -> int:
    self.parents = list(range(n))

    for edge in edges:
        self.union(edge[0], edge[1])

    return len({self.find(x) for x in range(n)})

def union(self, x, y):
    px, py = self.find(x), self.find(y)

    if px != py:
        self.parents[px] = py

def find(self, x) -> int:
    if self.parents[x] == x:
        return x
    return self.find(self.parents[x])

# https://leetcode.com/problems/graph-valid-tree/
def validTree(self, n: int, edges: list[list[int]]) -> bool:
    if not edges:
        return n == 1
    graph = collections.defaultdict(list)
    for edge in edges:
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])

    # dfs from any node should visit the whole graph, without cycles
    visited = set()

    def dfs(node, prev):
        if node in visited:
            return False

        visited.add(node)

        for nei in graph[node]:
            # can't go back on the same edge
            if nei != prev:
                if not dfs(nei, node): return False
        return True

    return dfs(edges[0][0], -1) and len(visited) == n

# https://leetcode.com/problems/pacific-atlantic-water-flow/
def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
    m, n = len(heights), len(heights[0])
    can_reach_pacific, can_reach_atlantic = [[-1 for _ in range(n)] for _ in range(m)], [[-1 for _ in range(n)] for
                                                                                            _ in range(m)]

    def dfs(x, y, is_reachable):
        if is_reachable[x][y] != -1:
            return

        is_reachable[x][y] = 1

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (i, j) in directions:
            if 0 <= x + i < m and 0 <= y + j < n:
                if heights[x + i][y + j] >= heights[x][y]:
                    dfs(x + i, y + j, is_reachable)

    for i in range(m):
        dfs(i, 0, can_reach_pacific)
        dfs(i, n - 1, can_reach_atlantic)

    for j in range(n):
        dfs(0, j, can_reach_pacific)
        dfs(m - 1, j, can_reach_atlantic)

    res = []
    for i in range(m):
        for j in range(n):
            if can_reach_pacific[i][j] == 1 and can_reach_atlantic[i][j] == 1:
                res.append([i, j])
    return res


# https://leetcode.com/problems/alien-dictionary/
# TODO: fix edge case
def buildGraph(self, words: list[str]):
    """
    Return alphabet, graph where alphabet is a set of unique letters and graph is an adjacency list and sources is nodes with no parents
    """

    def get_ordering(word_i, word_j):
        for char_i, char_j in zip(word_i, word_j):
            if char_i == char_j:
                continue
            return (char_i, char_j)

    edges = collections.defaultdict(list)
    parents = collections.defaultdict(list)
    alpha = set()
    for i in range(len(words) - 1):
        word_i, word_j = words[i], words[i + 1]
        ordering = get_ordering(word_i, word_j)
        if ordering:
            char_i, char_j = ordering
            edges[char_i].append(char_j)
            parents[char_j].append(char_i)

        alpha.update([c for c in word_i])
    alpha.update([c for c in words[-1]])

    sources = [node for node in alpha if not parents[node]]
    return alpha, edges, sources

def alienOrder(self, words: list[str]) -> str:
    alphabet, graph, sources = self.buildGraph(words)

    if not sources:
        return ""

    sorted_alphabet = []

    def dfs(node: str, visited, visiting) -> bool:  # return true if there's a cycle
        if node in visiting:
            return True

        visiting.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor, visited, visiting):
                    return True

        visiting.remove(node)
        visited.add(node)
        sorted_alphabet.append(node)
        return False

    visited, visiting = set(), set()
    for source in sources:
        if dfs(source, visited, visiting):
            return ""

    return "".join(reversed(sorted_alphabet)) if len(sorted_alphabet) == len(alphabet) else ""