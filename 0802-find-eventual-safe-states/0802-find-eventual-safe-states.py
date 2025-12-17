class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        self.stack = set()
        self.hash_map = {}
        ans = []
        
        for node in range(len(graph)):
            if self.dfs(node, graph):
                ans.append(node)
        
        return ans
    
    def dfs(self, node: int, graph: List[List[int]]) -> bool:

        if node in self.hash_map:
            return self.hash_map[node]
        
        if node in self.stack:
            return False
        
        self.stack.add(node)
        for neighbor in graph[node]:
            if not self.dfs(neighbor, graph):
                self.hash_map[node] = False
                return False
            
        self.stack.remove(node)
        self.hash_map[node] = True

        return True
        