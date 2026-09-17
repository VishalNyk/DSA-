class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n=len(nums)
        marker=[0]*(n+1)
        for i in nums:
            if(marker[i]==1):
                return i
            marker[i]=1
        return 0