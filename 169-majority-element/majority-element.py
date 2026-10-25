class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        ca=None
        c=0
        for n in nums:
            if c==0:
                ca=n
            c+=(1 if n==ca else -1)
        return ca