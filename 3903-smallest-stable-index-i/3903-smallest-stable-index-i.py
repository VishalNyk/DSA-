class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:

        #edge cases:
        if(len(nums)==0):
            return -1 
        if(len(nums)==1):
            return 0
        
        
        n=len(nums)
        prefix,suffix=[0]*n,[-1]*n
        current_max,current_min=0,float('inf')

        for i in range(n):
            current_max=max(current_max,nums[i])
            current_min=min(current_min,nums[n-1-i])

            prefix[i],suffix[n-1-i]=current_max,current_min

        for i in range(n):
            inscore=prefix[i]-suffix[i]
            if(inscore<=k):
                return i
        return -1
