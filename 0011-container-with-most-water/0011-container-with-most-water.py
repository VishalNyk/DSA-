class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left,right=0,len(heights)-1
        maxWater=0

        while(left<right):
            cheight=min(heights[left],heights[right])
            cArea=cheight*(right-left)

            if(cArea>maxWater):
                maxWater=cArea
            
            if(heights[left]<heights[right]):
                left+=1
            else:
                right-=1
        return maxWater