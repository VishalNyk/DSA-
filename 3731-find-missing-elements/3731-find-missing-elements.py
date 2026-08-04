class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        mi,mx=nums[0],nums[len(nums)-1]
        ans=[]
        while(mi<mx):
            if(mi not in nums):
                ans.append(mi)
            mi+=1
        return ans
