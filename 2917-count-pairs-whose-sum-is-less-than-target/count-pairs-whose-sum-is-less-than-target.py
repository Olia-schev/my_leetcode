class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ans = []
        inter = 0
        for i in range(len(nums)):
            my_list = [nums[j]+nums[i] for j in range(i+1,len(nums))]
            for k in my_list:
                if k<target:
                    inter += 1
            ans.append(inter)
        return max(ans)
            
            
    

        