class Solution(object):
    def countConsistentStrings(self, allowed, words):
        end = 0
        for i in words:
            test = []
            for k in allowed:
                ans = []
                list(map(lambda x: ans.append(x ==k),i))
                test.append(sum(ans))
            if sum(test)==len(i):
                end = end+1

        return end




        
        