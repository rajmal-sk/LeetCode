class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = set()
        nums = sorted(nums)

        def twoSum(left, right, target) ->  List[List[int]]:
            pairs = []
            while(left < right):
                sum = nums[left] + nums[right]
                if sum > target:
                    right -= 1
                elif sum < target:
                    left += 1
                else:
                    pairs.append([left, right])
                    left += 1
                    right -= 1

            return pairs
        

        for i in range(n-2):
            target = 0 - nums[i]

            pairs = twoSum(i+1, n-1, target)


            if len(pairs) > 0:
                for j, k in pairs:
                    res.add((nums[i], nums[j], nums[k]))
        
        return list(res)




