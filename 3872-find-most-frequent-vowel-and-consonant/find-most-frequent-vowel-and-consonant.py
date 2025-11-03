class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o','u']
        my_dict = {}
        for i in s: 
            if i in my_dict:
                my_dict[i] += 1
            else:
                my_dict[i] = 1
        list_val = [0]
        list_cons = [0]
        for v in my_dict:
            if v in vowels:
                list_val.append(my_dict[v])
            else:
                list_cons.append(my_dict[v])

        return max(list_val) + max(list_cons)
        