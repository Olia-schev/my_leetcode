class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        summ = []
        for i in range(len(nums)):
            if i%2 == 0:
                summ.append(nums[i])
            else: 
                summ.append(-nums[i])
        return sum(summ)
        