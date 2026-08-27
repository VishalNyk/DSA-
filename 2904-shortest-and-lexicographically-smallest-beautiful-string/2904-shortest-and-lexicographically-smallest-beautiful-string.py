class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:

        #edge case
        if(s.count("1")<k):
            return ""
        
        ans=""
        minlen=float('inf')
        l,ones=0,0

        for r in range(len(s)):
            if(s[r]=='1'):
                ones+=1
            while(ones==k):
                clen=r-l+1
                csub=s[l:r+1]
                if(clen<minlen):
                    minlen=clen
                    ans=s[l:r+1]
                elif(clen==minlen and csub<ans):
                    ans=csub
                
                if(s[l]=='1'):
                    ones-=1
                l+=1
        return ans



        
        