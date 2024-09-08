class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        students.sort()
        ans = 0
        for i in students:
            min_seats = min(seats)
            ans += abs(i-min_seats)
            seats.remove(min_seats)
        return ans

            
            

        return ans
        