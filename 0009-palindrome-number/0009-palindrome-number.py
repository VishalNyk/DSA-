class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        sr=s[::-1]
        if(s==sr):
            return True
        return False

        