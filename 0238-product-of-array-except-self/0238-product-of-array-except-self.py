class Solution:
    
    # Video Link: https://www.youtube.com/watch?v=bNvIQI2wAjk
    
    # With division operator
    # Time complexity: O(N)
    # Space Complexity: O(1)
        
    """"def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        product = 1
        # if i is zero then we need the product without zero 
        zero_product = 1
        zero_count = 0
        
        for i in range(len(nums)):
            product *= nums[i]
            if nums[i] != 0:
                zero_product *= nums[i]
            if nums[i] == 0:
                zero_count += 1
            
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = product//nums[i]
            elif zero_count < 2:
                nums[i] = zero_product
            else:
                nums[i] = 0
            
        return nums"""
    
    """# Using Extra Space
    # Space Complexity: O(N)
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1]*n
        postfix = [1]*n
        
        # Compute prefixes and postfixes
        for i in range(1,n):
            prefix[i] = prefix[i-1]*nums[i-1]
            postfix[~i] = postfix[~i+1]*nums[~i+1]
         
        # Compute result by multiplying prefix with postfix
        for i in range(n):
            nums[i] = prefix[i]*postfix[i]
            
        return nums"""
    
    # Without Extra Space
    # Space Complexity: O(1)
    def productExceptSelf1(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        output = [1]*len(nums)
        
        # Compute the prefix and store in output array
        for i in range(1, n):
            output[i] = output[i-1]*nums[i-1]
         
        postfix = nums[-1]
        
        # Compute result
        for i in range(n-2, -1, -1):
            output[i] = output[i]*postfix
            postfix *= nums[i]
        
        return output
    
    
    # Space Complexity: O(1)
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        
        for num in nums:
            if num == 0:
                num_zeros += 1
                continue
            product *= num
        
        output = [0]*n
        for i, num in enumerate(nums):
            # if there is one zero in the input then for num zero the product 
            # will be the product of all other elements in array
            # e.g. [-1,1,0,-3,3]
            # and for remaning elements the product will become zero due to this
            # one zero in array
            # and if the number of zeros are more than 1 then for every element
            # the product will become zero e.g [0,4,0,1,2]
            if num == 0 and num_zeros == 1:
                output[i] = product
            # if there is no zero in the input then the product for each element
            # will be equal to product of all elements divided by that number 
            # e.g. 
            elif num_zeros == 0:
                output[i] = int(product/num)
        
        return output
    
    # If we are allowed to update original array
    def productExceptSelf3(self, nums: List[int]) -> List[int]:
        product = 1
        num_zeros = 0
        
        for num in nums:
            if num == 0:
                num_zeros += 1
                continue
            product *= num
        
        for i, num in enumerate(nums):
            if num == 0 and num_zeros == 1:
                nums[i] = product
            # if there is no zero in the input then the product for each element
            # will be equal to product of all elements divided by that number 
            # e.g. 
            elif num_zeros == 0:
                nums[i] = product//num
            else:
                nums[i] = 0
        
        return nums
    
    def productExceptSelf4(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix_product = [1]*len(nums)
        postfix_product = [1]*len(nums)

        # compute prefix and prostfix product
        for i in range(1,len(nums)):
            prefix_product[i] = nums[i-1]*prefix_product[i-1]
            if n-i-1 < n-1:
                postfix_product[n-i-1] = nums[n-i]*postfix_product[n-i]

        # final product
        for i in range(len(nums)):
            nums[i] = prefix_product[i]*postfix_product[i]

        return nums
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        output = [1]
        
        for i in range(1, len(nums)):
            output.append(output[-1]*nums[i-1])
        
        postfix_product = 1
        
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix_product
            postfix_product *= nums[i]
        
        return output
                
                
        