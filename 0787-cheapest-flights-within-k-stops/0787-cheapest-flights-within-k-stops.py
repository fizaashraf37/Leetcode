class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        adj_list = [[] for _ in range(n)]

        for node, neighbor, price in flights:
            adj_list[node].append([neighbor, price])
        
        min_heap = [(0, -1, src)] # price, stops, node
        costs = [(float("inf"), 0)]*n

        while min_heap:
            price, stops, node = heappop(min_heap)
            if node == dst and stops <= k:
                return price
            if stops >= k:
                continue
            for neighbor, neighbor_cost in adj_list[node]:
                dest_cost, dest_stops = price+neighbor_cost, stops+1 
                if dest_cost >= costs[neighbor][0] and dest_stops >= costs[neighbor][1]:
                    continue
                heappush(min_heap, (price+neighbor_cost, stops+1, neighbor))
                costs[neighbor] = [dest_cost, dest_stops]
        
        return -1