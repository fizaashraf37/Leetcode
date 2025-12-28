class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:

        def dfs(root:int, node: int) -> None:

            if node in visited:
                return
            
            visited.add(node)
            ans[node] = root

            for neighbor in adj_list[node]:
                dfs(root, neighbor)
                

        adj_list = [[] for _ in range(len(quiet))]
        ans = [0]*len(quiet)

        for node, neighbor in richer:
            adj_list[node].append(neighbor)
        
        visited = set()

        sorted_queit = sorted(enumerate(quiet), key=lambda x: x[1])

        for i in range(len(sorted_queit)):
            dfs(sorted_queit[i][0], sorted_queit[i][0])
        
        return ans

        

        