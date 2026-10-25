class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)
        ans=[]

         for i in range(n-2):
        #     This is a mathematical optimization. Because the array is already sorted in ascending order, 
        #     if your current anchor number nums[i] is strictly greater than zero, every single number remaining to its right will also be positive.
        #     hence adding +ve nos. will never yield 0
            if(nums[i]>0):
                break
            # Since nums is sorted, hence high chance same items can pollute the actual triplet
            if(i>0 and nums[i]==nums[i-1]):
                continue
            
            left=i+1
            right=n-1
            while(left<right):
                currentSum=nums[i]+nums[left]+nums[right]
                if(currentSum<0):
                    left+=1
                elif(currentSum>0):
                    right-=1
                else:
                    ans.append([nums[i],nums[left],nums[right]])

                    left+=1
                    right-=1

                    while(left<right and  nums[left]==nums[left-1]):
                        left+=1
                    while(left<right and nums[right]==nums[right+1]):
                        right-=1
        return ans


                

        
