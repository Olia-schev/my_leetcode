class Solution(object):
    def numberGame(self, nums):
        arr = []
        for i in range(len(nums)):
             try:
                Alice = min(nums)
                nums.remove(min(nums))
                Bob = min(nums)
                nums.remove(min(nums))
                arr.append(Bob)
                arr.append(Alice)
             except:
                break
        return arr


        