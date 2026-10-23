class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        st=s.split()
        if(len(pattern)!=len(st)):
            return False
        
        di={}
        seen=set()

        for char_p, word in zip(pattern,st):
            if(char_p in di and di[char_p]!=word):
                return False
            else:
                if(char_p not in di and word in seen):
                    return False
                
                di[char_p]=word
                seen.add(word)
        return True