class Solution:
    def firstUniqChar(self, s: str) -> int:
        f={}
        for x in s:
            f[x]=f.get(x,0)+1
        for i,x in enumerate(s):
            if f[x]==1:
                return i
        return -1