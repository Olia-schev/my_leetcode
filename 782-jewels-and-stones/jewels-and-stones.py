class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        a = 0
        for i in jewels:
            a += sum(list(map(lambda x: 1 if x==i else 0,stones)))
        return a
        