class Solution(object):
    def createTargetArray(self, nums, index):
        ans = []
        for i in range(len(nums)):
            ans.insert(index[i], nums[i])
        return ans


        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        