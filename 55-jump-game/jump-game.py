class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = False
        destIdx = len(nums) - 1
        currIdx = destIdx - 1
        while currIdx >= 0:
            if currIdx + nums[currIdx] >= destIdx:
                destIdx = currIdx

            currIdx -= 1
        return destIdx == 0