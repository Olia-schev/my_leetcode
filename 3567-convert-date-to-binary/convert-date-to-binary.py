class Solution(object):
    def convertDateToBinary(self, date):
        year = bin(int(date[0:4]))[2:]
        mounth = bin(int(date[5:7]))[2:]
        day = bin(int(date[8:10]))[2:]
        ans = [year,mounth,day]
        return '-'.join(ans)