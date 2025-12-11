"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:

        adj_list, target_employee = self.build_adj_list(employees, id)
        return self.bfs(adj_list, target_employee)

    def build_adj_list(self, employees: List['Employee'], id: int):

        adj_list = defaultdict(list['Employee'])
        target_employee = None

        hashmap = defaultdict()
        for employee in employees:
            if employee.id == id:
                target_employee = employee
            hashmap[employee.id] = employee
        
        for employee in employees:
            if employee.id == id:
                target_employee = employee
            for subordinate in employee.subordinates:
                adj_list[employee.id].append(hashmap[subordinate])
        
        return adj_list, target_employee
    
    def bfs(self, adj_list: dict[List], target_employee: 'Employee') -> int:
        queue = deque([target_employee])
        importance = 0

        while queue:
            cur_node = queue.popleft()
            importance += cur_node.importance
            for neighbor in adj_list[cur_node.id]:
                queue.append(neighbor)
        
        return importance

        