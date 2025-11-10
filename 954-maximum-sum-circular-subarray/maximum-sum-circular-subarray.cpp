class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
       int totalSum = 0;
       int maxSum = INT_MIN;
       int minSum = INT_MAX;
       int currSum1 = 0;
       int currSum2 = 0;

       for(int i = 0; i<nums.size(); i++)
       {
        totalSum += nums[i];
        currSum1 += nums[i];
        currSum2 += nums[i];

        maxSum = max(maxSum, currSum1);
        if(currSum1 < 0) currSum1 = 0;
        minSum = min(minSum, currSum2);
        if(currSum2 > 0) currSum2 = 0;
       } 

       return totalSum == minSum ? maxSum : max (maxSum, totalSum - minSum);
    }
};