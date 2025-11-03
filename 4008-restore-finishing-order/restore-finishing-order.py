class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        list_friends = []
        for i in order:
            if i in friends:
                list_friends.append(i)
        return list_friends
        