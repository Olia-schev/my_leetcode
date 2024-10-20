class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ans =[]
        for i in nums:
            zie = 0
            for j in nums:
                if i!=j and j<i:
                    zie = zie+1
            ans.append(zie)
        return ans

