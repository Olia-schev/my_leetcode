class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total_xor_sum = 0
        for i in range(1 << len(nums)):  # Цикл по всем возможным подмножествам
            subset_xor = 0
            for j in range(len(nums)):  # Цикл по элементам массива
                if (i >> j) & 1:  # Проверка, присутствует ли j-й элемент в подмножестве
                     subset_xor ^= nums[j]  # Вычисление XOR-суммы подмножества
            total_xor_sum += subset_xor  # Добавление XOR-суммы подмножества к общей сумме
        return total_xor_sum
     
        

        