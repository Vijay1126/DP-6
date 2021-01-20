class Ugly:
    def __init__(self):
        self.nums = nums = [1]
        num1 = 2
        num2 = 3
        num3 = 5
        
        p1 = 0
        p2 = 0
        p3 = 0
        
        i = 1

        while i<1690:
            currMin = min(nums[p1]*2, nums[p2]*3, nums[p3]*5)
            nums.append(currMin) 
            i+=1
            if currMin == nums[p1]*2:
                p1+=1
            if currMin == nums[p2]*3:
                p2+=1
            if currMin == nums[p3]*5:
                p3+=1
            
class Solution:
    ugly = Ugly()
    def nthUglyNumber(self, n: int) -> int:
        return self.ugly.nums[n-1]
Time: O(1)
Space: Constant Space
