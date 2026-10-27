class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        mx=nums[0]
        s=nums[0]
        x=s+mx
        for i in range(1,len(nums)):
            s=max(nums[i],s+nums[i])
            mx=max(mx,s)
            
    
        return mx       
            
