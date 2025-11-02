class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Cumulative sums and their frequency 
        counts = defaultdict(int)

        # Initialization where the frequency of sum 0 is 1 by default - Empty subarray
        counts[0] = 1
        currSum = ans = 0

        for num in nums:
            # Increment the cumulative sum
            currSum += num
            # Check if target in the counts hashmap
            target = currSum - k
            if target in counts:
                ans += counts[target]

            counts[currSum] += 1
        return ans
