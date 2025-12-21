class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:

        adj_list = [[] for _ in range(n)]

        for node, neighbor, time in roads:
            adj_list[node].append([neighbor, time])
            adj_list[neighbor].append([node, time])
        
        times = [float("inf")]*n
        min_heap = [(0, 0)]
        ways = [0]*n
        ways[0] = 1

        while min_heap:
            time, node = heappop(min_heap)
            
            if node == n-1:
                break
            
            for neighbor, neighbor_time in adj_list[node]:
                new_time = time + neighbor_time
                if new_time < times[neighbor]:
                    ways[neighbor] = ways[node]
                    heappush(min_heap, (new_time, neighbor))
                    times[neighbor] = new_time
                elif new_time == times[neighbor]:
                    ways[neighbor] += ways[node]
        
        return ways[n-1] % (1000000007)
            