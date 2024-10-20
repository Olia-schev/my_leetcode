class Solution(object):
    def sumIndicesWithKSetBits(self, nums, k):
        ans = 0
        for i in range(len(nums)) :
            bit = sum(map(int, list(str(format(i, 'b')))))
            if bit == k:
                ans = ans+ nums[i]
        return ans
        