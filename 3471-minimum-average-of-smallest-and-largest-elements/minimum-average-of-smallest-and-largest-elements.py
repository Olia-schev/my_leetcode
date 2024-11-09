class Solution(object):
    def minimumAverage(self, nums):
        averages = []
        for i in range(1,len(nums)):
            try:
                mins = min(nums)
                maxi = max(nums)
                averages.append((mins+maxi)/2.0)
                nums.remove(mins)
                nums.remove(maxi)
            except:
                break
        return min(averages)