class Solution(object):
    def theMaximumAchievableX(self, num, t):
        ans = []
        for i in [0,2,-2]:
            ans.append(num+i*t)
        return max(ans)
        