class Solution(object):
    def sortPeople(self, names, heights):
        heights2 = sorted(heights,reverse=True)
        ans = []
        for i in range(len(heights)):
            ans.append(names [heights.index(heights2[i])])
        return ans
        