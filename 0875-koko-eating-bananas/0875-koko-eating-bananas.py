class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculate_hours(speed: int) -> int:

            hours = 0

            for pile in piles:
                hours += math.ceil(pile/speed)
            
            return hours

        low, high = 1, max(piles)

        while low <= high:
            speed = low + (high - low) // 2
            hours = calculate_hours(speed)
            if hours <= h:
                high = speed - 1
            else:
                low = speed + 1

        return low

        