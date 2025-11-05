class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums.sort()
        longeststreak = 1
        currentstreak = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    currentstreak += 1
                else:
                    longeststreak = max(longeststreak, currentstreak)
                    currentstreak = 1
        
        return max(longeststreak, currentstreak)
