class Solution:
    def trap(self, height: List[int]) -> int:
        # Intution: For each index i the amount of water that can be stored equals 
        # min(leftMax, rightMax) - height[i]
        # leftMax - represents the highest point on the left of the index i
        # rightMax - represents the highest point on the right of the index i
        n = len(height)
        left, right = 0, n - 1
        leftMax = rightMax = water = 0 

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                water += (leftMax - height[left])
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                water += (rightMax - height[right])
                right -= 1
       
        
        return water
        