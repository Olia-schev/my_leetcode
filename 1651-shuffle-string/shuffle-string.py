class Solution(object):
    def restoreString(self, s, indices):
        ans = list(map(lambda x:'', range(len(s))))
        for i in range(len(indices)):
            ans[indices[i]] = s[i]
     
        return ''.join(ans)