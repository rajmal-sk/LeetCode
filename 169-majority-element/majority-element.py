class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        candidate = nums[0]
        freq = 1
        for i in range(1, len(nums)):
            if nums[i] == candidate:
                freq += 1       
            elif freq > 0:
                freq -= 1           
            else:
                freq = 1
                candidate = nums[i]       
        return candidate