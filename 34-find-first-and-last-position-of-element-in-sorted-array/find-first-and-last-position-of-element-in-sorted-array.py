class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        lf=self.findBound(nums,target,isf=True)
        if lf==-1:
            return [-1,-1]
        rf=self.findBound(nums,target,isf=False)
        return [lf,rf]
    def findBound(self,nums,target,isf):
        l=0
        h=len(nums)-1
        bo=-1
        while l<=h:
            mid=l+(h-l)//2
            if nums[mid]==target:
                bo=mid
                if isf:
                    h=mid-1
                else:
                    l=mid+1
            elif nums[mid]<target:
                l=mid+1
            else:
                h=mid-1
        return bo