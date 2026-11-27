from collections import defaultdict

class Graph:
    
    # dict of directed edges. key is src, val is set of dsts
    def __init__(self):
        self.edges = defaultdict(set)   # allows reduced clunky exist checks for adds

    # add edge from src to dst -- if either node doesn't exist, add them
    def addEdge(self, src: int, dst: int) -> None:
        self.edges[src].add(dst)

    # remove if exists, return whether removed. either node may not exist
    def removeEdge(self, src: int, dst: int) -> bool:        
        if dst in self.edges[src]:
            self.edges[src].remove(dst)
            return True
        return False

    # DFS through dict
    def hasPath(self, src: int, dst: int) -> bool:
        visited = set() # avoiding infinite search

        def dfs(cur):
            # invariant: vertices we recurse on must be tracked
            nonlocal visited
            visited.add(cur)

            if dst in self.edges[cur]:
                return True

            for edge in self.edges[cur]:
                if edge not in visited:
                    if dfs(edge):
                        return True
            
            return False

        return dfs(src)

