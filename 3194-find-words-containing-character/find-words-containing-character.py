class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        index_list = []
        for i in range(len(words)):
            if words[i].__contains__(x):
                index_list.append(i)
        return(index_list)

        