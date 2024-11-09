class Solution(object):
    def truncateSentence(self, s, k):
        return ' '.join(s.split(' ')[0:k])
