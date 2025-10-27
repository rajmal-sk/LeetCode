class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        leftMax = [0] * n
        rightMax = [0] * n

        maxi = float('-inf')
        for i in range(n):
            leftMax[i] = max(maxi, height[i])
            maxi = max(maxi, height[i])
        
        maxi = float('-inf')
        for i in range(n-1, -1, -1):
            rightMax[i] = max(maxi, height[i])
            maxi = max(maxi, height[i])
        
        waterContent = 0

        for i in range(n):
            capacity = min(leftMax[i], rightMax[i]) - height[i]
            waterContent += capacity
        
        return waterContent
        