class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = [[position[i], speed[i]] for i in range(len(position))]
        cars.sort(key=lambda x: x[0], reverse=True)
        fleets = 0
        stack = []

        for i in range(len(cars)):
            position, speed = cars[i]
            time_to_reach_target = (target-position)/speed
            while stack and time_to_reach_target > stack[-1]:
                stack.pop()
            if not stack:
                stack.append(time_to_reach_target)
                fleets += 1
        
        return fleets