class Solution(object):
    def numberOfPairs(self, nums1, nums2, k):
        ans = 0 
        for i in nums1:
            for j in nums2:
                if (i % (j*k)) ==0:
                    ans = ans+1
        return ans
        