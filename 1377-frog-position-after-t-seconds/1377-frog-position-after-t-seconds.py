class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:

        adj_list = self.build_adj_list(edges, n)
        return self.bfs(adj_list, target-1, t)

    def build_adj_list(self, edges: List[List[int]], n: int):

        adj_list = [[] for _ in range(n)]

        for node, neighbor in edges:
            adj_list[node-1].append(neighbor-1)
            adj_list[neighbor-1].append(node-1)
        
        return adj_list
    
    def bfs(self, adj_list: List[List[int]], target:int, t: int) -> int:

        queue = deque([[0, 1, t]])
        visited = set()

        while queue:
            cur_node, probability, time = queue.popleft()
            if cur_node == target and time == 0:
                return probability
            visited.add(cur_node)
            neighbor_count = 0
            for neighbor in adj_list[cur_node]:
                if neighbor not in visited:
                    neighbor_count += 1
            if neighbor_count == 0 and cur_node == target and time >= 0:
                return probability
            for neighbor in adj_list[cur_node]:
                if neighbor not in visited:
                    jump_probability = probability*1/max(1, neighbor_count)
                    queue.append([neighbor, jump_probability, time-1])
        
        return 0