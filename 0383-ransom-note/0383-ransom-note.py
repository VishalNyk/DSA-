class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote)>len(magazine)):
            return False
        
        inventory=[0]*26
        for char in magazine:
            index=ord(char)-ord('a')
            inventory[index]+=1
        
        for char in ransomNote:
            index=ord(char)-ord('a')
            if(inventory[index]==0):
                return False
            else:
                inventory[index]-=1
        return True