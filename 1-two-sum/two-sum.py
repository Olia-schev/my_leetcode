class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_list = []
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if i==j:
                    continue
                else:
                    if nums[i]+nums[j]==target:
                        my_list.append(i)
                        my_list.append(j)
        return list(set(my_list))
        