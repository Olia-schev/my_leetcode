class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(0,2):
            list(map(lambda x: ans.append(x) ,nums))
        return ans
        