class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        lastNum = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            if nums[i] == lastNum:
                freq += 1
            
            if nums[i] != lastNum and freq > 0:
                freq -= 1
            
            if nums[i] != lastNum and freq == 0:
                freq = 1
                lastNum = nums[i]
        
        return lastNum