class Solution(object):
    def leftRightDifference(self, nums):
        ans =[] 
        for i in range(len(nums)):
            ans.append(abs(sum(nums[0:i])-sum(nums[i+1:len(nums)]) ))
        return ans
       