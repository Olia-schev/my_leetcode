class Solution(object):
    def smallestEvenMultiple(self, n):  
        a = 2
        m = a * n
        while a != 0 and n != 0:
            if a > n:
                a %= n
            else:
                n %= a
        return m // (a + n)