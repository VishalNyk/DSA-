class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n=len(nums)
        marker=[False]*(n+1)
        for i in nums:
            if(marker[i]):
                return i
            marker[i]=True
        return 0