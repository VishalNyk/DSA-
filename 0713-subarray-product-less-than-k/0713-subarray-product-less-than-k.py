class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left,count=0,0

        if(k<=1):
            return 0
        prd=1
        for right in range(len(nums)):
            prd=prd*nums[right]

            while(prd>=k):
                prd=prd//nums[left]
                left+=1
            count+=right-left+1
    
        return count