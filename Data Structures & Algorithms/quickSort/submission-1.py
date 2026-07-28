# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        """ implementation of the quicksort algorithm"""
        self.quickSortHelper(pairs, 0, len(pairs)-1)
        return pairs
        
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:

        if e -  s + 1 <= 1:
            return 
        
        
        pivot = arr[e]
        l = s
        for index in range(s,e):
            if arr[index].key < pivot.key:
                tmp = arr[l]
                arr[l] = arr[index]
                arr[index] = tmp
                l+=1
        
        arr[e], arr[l] = arr[l], arr[e]
        self.quickSortHelper(arr, s, l-1)
        self.quickSortHelper(arr, l+1, e)
