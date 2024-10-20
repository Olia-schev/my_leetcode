class Solution(object):
    def getSneakyNumbers(self, nums):
        ans = []
        for i in range(len(nums)):
            list(map(lambda x: ans.append(x) if x==nums[i] else "",nums[i+1:len(nums)]))
        return ans


        
        