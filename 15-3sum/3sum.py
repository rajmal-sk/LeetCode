class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        # Python uses a version of TimSort which takes O(NLogN) - TC and 
        nums.sort()
        
        # Take O(N) time complexity - Since we are doing a single pass to
        # identify all the valid pairs
        def twoSum(i):
            left, right = i + 1, n - 1
            target = -nums[i]

            while(left < right):
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        for i in range(n-2):
            # Not possible to find a pair to complement nums[i]
            # since all the future elements would be greater than 0.
            if nums[i] > 0:
                break

            if i == 0 or nums[i - 1] != nums[i]:
                twoSum(i)
        
        return list(res)




