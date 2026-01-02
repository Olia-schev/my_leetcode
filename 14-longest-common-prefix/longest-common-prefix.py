class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        from collections import Counter
        if len(strs) == 1:
            return strs[0]
        else:
            prifix = []
            for i in strs:
                a = ''
                for k in range(len(i)):
                 try:
                        a += i[k]
                        prifix.append(a)
                 except:
                      continue
            try:
                # max_count = Counter(prifix).most_common(1)[0][1]
                counter_prifix  = Counter({k: v for k, v in Counter(prifix).items() if (v >= len(strs)) & (v != 1)})
                return max(counter_prifix, key=len)
            except: 
                return ""
        