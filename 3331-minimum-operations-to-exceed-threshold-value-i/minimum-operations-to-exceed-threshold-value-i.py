class Solution(object):
    def minOperations(self, nums, k):
        nums.sort()
        ans = len(list(filter(None,
         list(map(lambda x:x if x< k else nums.remove(x), nums)))))
        return ans
            


        
        