class Solution(object):
    def decompressRLElist(self, nums):
        ans = []
        for i in range(len(nums)):
            if i%2 == 0:
                 ans = ans + list(map(lambda x:nums[i+1] , range(nums[i]))) 
            else:
                continue
        return ans
        
        