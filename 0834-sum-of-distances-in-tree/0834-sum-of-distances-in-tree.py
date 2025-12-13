class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:

        adj_list = self.build_adj_list(edges, n)
        self.counts = [0]*n
        self.distance_sum = [0]*n

        self.preorder(0, adj_list, -1)
        self.postorder(0, adj_list, n, -1)

        return self.distance_sum


    def preorder(self, node: int, adj_list: List[List[int]], parent: int):

        total_sum, nodes_count = 0, 1
        for child in adj_list[node]:
            if child == parent:
                continue
            subtree_sum, count = self.preorder(child, adj_list, node)
            total_sum += subtree_sum + count
            nodes_count += count

        self.counts[node] = nodes_count
        self.distance_sum[node] = total_sum

        return total_sum, nodes_count
    
    def postorder(self, node: int, adj_list: List[List[int]], n: int, parent: int):

        for child in adj_list[node]:
            if child == parent:
                continue
            self.distance_sum[child] = self.distance_sum[node] - self.counts[child] + (n-self.counts[child])
            self.postorder(child, adj_list, n, node)

    def build_adj_list(self, edges: List[List[int]], n:int):

        adj_list = [[] for _ in range(n)]
        for node, neighbor in edges:
            adj_list[node].append(neighbor)
            adj_list[neighbor].append(node)
        
        return adj_list
        




        
        