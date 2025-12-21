class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adj_list = self.build_graph(times, n)
        min_heap = [(0, k-1)]
        min_delay_time = 0
        visited = set()

        while min_heap:
            node_time, node = heappop(min_heap)
            if node in visited:
                continue
            visited.add(node)
            min_delay_time = max(min_delay_time, node_time)
            for neighbor, time in adj_list[node]:
                heappush(min_heap, (node_time + time, neighbor))

        return min_delay_time if len(visited) == n else -1

        
    def build_graph(self, times: List[List[int]], n: int) -> List[List[int]]:

        adj_list = [[] for _ in range(n)]

        for node, neighbor, time in times:
            adj_list[node-1].append([neighbor-1, time])
        
        return adj_list