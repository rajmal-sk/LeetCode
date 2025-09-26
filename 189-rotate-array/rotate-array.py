class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # First Half
        i = 0
        j = n - k - 1
        while(i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        
        # Second Half
        i = n - k
        j = n - 1
        while(i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        # reverse

        nums.reverse()