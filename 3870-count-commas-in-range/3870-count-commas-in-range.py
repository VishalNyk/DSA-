class Solution:
    def countCommas(self, n: int) -> int:
        l=len(str(abs(n)))
        if(l<=3):
            return 0
        #base=int("1"+"0"*(l-1))

        return n-1000+1

        