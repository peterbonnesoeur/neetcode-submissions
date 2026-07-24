class Solution:
    def countElements(self, arr: List[int]) -> int:
        """
            Count the amount of times an index have a follower element
            Args:
                arr: list[int]
        """
        arr_set = Counter(arr)
        count = 0
        for key in arr_set:
            if key+1 in arr_set:
                count += arr_set[key]

        return count