class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = ''
        for i in range(-1,-len(str(x))-1,-1):
            y += str(x)[i]
        if str(x) == y:
            return True
        else:
            return False
        