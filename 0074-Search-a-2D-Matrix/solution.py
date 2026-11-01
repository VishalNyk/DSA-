class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row,col=len(matrix),len(matrix[0])
        left,right=0,row*col-1
        while(left<=right):
            mid=(left+right)//2
            midval=matrix[mid//col][mid%col]
            if(midval==target):
                return True
            elif(midval<target):
                left=mid+1
            else:
                right=mid-1
        return False