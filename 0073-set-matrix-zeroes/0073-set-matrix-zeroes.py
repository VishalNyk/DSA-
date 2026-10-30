class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n,m=len(matrix),len(matrix[0])

        #traversing and finding all locations
        indexes=[]
        for i in range(n):
            for j in range(m):
                if(matrix[i][j]==0):
                    indexes.extend([i,j])
        #applying 0 transform at given locations
        Zrows=indexes[::2]
        Zcols=indexes[1::2]
        for i in range(n):
            for j in range(m):
                if(i in Zrows or j in Zcols):
                    matrix[i][j]=0
        return
        