class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        prev = -1
        for i in range(len(arr)-1, -1, -1):
            if prev == -1:
                curr = arr[i]
                arr[i] = prev
                prev = curr
            else:
                if prev > arr[i]:
                    arr[i] = prev
                else:
                    curr = arr[i]
                    arr[i] = prev
                    prev = curr
        
        return arr