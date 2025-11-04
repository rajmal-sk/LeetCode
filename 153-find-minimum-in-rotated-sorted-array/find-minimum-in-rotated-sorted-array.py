class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            if l == r:
                return nums[l]
            
            mid = (l + r) // 2

            if nums[mid] < nums[r]:
                r = mid

            else:
                l = mid + 1
        
