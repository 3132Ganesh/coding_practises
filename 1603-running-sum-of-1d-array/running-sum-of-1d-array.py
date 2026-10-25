class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        r=[]
        cs=0
        for num in nums:
            cs+=num
            r.append(cs)
            
        return r        