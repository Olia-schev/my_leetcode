class Solution:
    def romanToInt(self, s: str) -> int:
        dict_num = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exceptions = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        sum = 0
        exc_letter = []

        for k in exceptions.keys():
            try:
                sum += exceptions[re.findall(k,s)[0]]
                exc_letter.append(k)
            except: 
                continue
        s_new = s
        for l in exc_letter:
            s_new = s_new .replace(l,'')

        for i in s_new:
            sum += dict_num[i]
        return sum