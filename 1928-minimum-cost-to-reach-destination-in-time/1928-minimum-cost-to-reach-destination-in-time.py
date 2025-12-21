class Solution:
    def minCost(self, maxTime: int, edges: List[List[int]], passingFees: List[int]) -> int:

        n = len(passingFees)
        adj_list = [[] for _ in range(n)]

        for node, neighbor, time in edges:
            adj_list[node].append([neighbor, time])
            adj_list[neighbor].append([node, time])
        
        min_heap = [(passingFees[0], 0, 0)] # fee, time, node
        times_and_fees = [[passingFees[0], float("inf")]]*n

        while min_heap:
            fee, time, node = heappop(min_heap)
            if node == n-1 and time <= maxTime:
                return fee
            for neighbor, neighbor_time in adj_list[node]:
                dest_time, dest_fee = time + neighbor_time, fee + passingFees[neighbor]
                if dest_fee >= times_and_fees[neighbor][0] and dest_time >= times_and_fees[neighbor][1] or dest_time > maxTime:
                    continue
                heappush(min_heap, (dest_fee, dest_time, neighbor))
                times_and_fees[neighbor] = [dest_fee, dest_time]
        
        return -1

        