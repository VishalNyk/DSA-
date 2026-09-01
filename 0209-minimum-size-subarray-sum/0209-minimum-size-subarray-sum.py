class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left,sm=0,0
        sl=float('inf')

        for right in range(len(nums)):
            sm+=nums[right]

            while(sm>=target):
                sl=min(sl, right-left+1)
                sm-=nums[left]
                left+=1
        if(sl!=float('inf')):
            return sl
        else:
            return 0    
        