class Solution:
    def minMoves(self, balance: List[int]) -> int:

        left, right = 0, 0
        left_distance, right_distance = 1, 1
        n = len(balance)

        for i in range(n):
            if balance[i] < 0:
                left = n-1 if i-1 < 0 else i-1
                right = (i+1)%n
                break   

        steps = 0
        
        while balance[i] < 0:
            while balance[left] == 0 and left != i:
                left = n-1 if left-1 < 0 else left-1
                left_distance += 1
            while balance[right] == 0 and right != i:
                right = ((right+1) % n)
                right_distance += 1
            if left == right == i:
                return -1
            if left_distance < right_distance:
                cur_balance = min(balance[left], abs(balance[i]))
                balance[i] += cur_balance
                balance[left] -= cur_balance
                steps += cur_balance*left_distance
            else:
                cur_balance = min(balance[right], abs(balance[i]))
                balance[i] += cur_balance
                balance[right] -= cur_balance
                steps += cur_balance*right_distance

        return steps

        # [2,3,1,1,-4,1,2,4,1,2,4,5]
        # [2,3,1,2,-4,-3,2,3,4,-5,1,2,4,5]
        #  8,9,2,2,-4,-3,2,3,4,-5

        # [2,3,1,1,-4,-3,1,2,4,-5,1,2,4,5]
        # [2,3,0,0,-4,-3,0,1,0,-5,0,0,4,5]
        #    ^                        ^
        # 1+2+2+3 
        # 9
        # 1+4+6

        # if distance to left and right is same then pick smaller value
        
        # 10,12,3,4
        
        