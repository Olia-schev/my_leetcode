class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            count = i%3
            if count == 0:
                ans += 0
            elif count >= 1:
                ans += 1
        return(ans)

            

        print(my_list)
        return(my_list)

        

        