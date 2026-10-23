class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        dic={}
        seen=set()

        for i in range(len(s)):
            if(s[i] in dic):
                if(dic[s[i]]!=t[i]):
                    return False
            else:
                if(t[i] in seen):
                    return False
                
                dic[s[i]]=t[i]
                seen.add(t[i])
        return True

