# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        # if len(pairs) == 2:
        #     if pairs[0].key > pairs[1].key:
        #         pairs[0], pairs[1] = pairs[1], pairs[0]
        #     return pairs


        middle = len(pairs) // 2
        res = []
        left_side = self.mergeSort(pairs[:middle])
        right_side = self.mergeSort(pairs[middle:])
        l, r = 0,0

        while l < len(left_side) and r < len(right_side):

            if left_side[l].key <= right_side[r].key:
                res.append(left_side[l])
                l+=1
            else:
                res.append(right_side[r])
                r+=1

        while l < len(left_side):
            res.append(left_side[l])
            l+=1

        while r < len(right_side):
            res.append(right_side[r])
            r+=1

        return res

