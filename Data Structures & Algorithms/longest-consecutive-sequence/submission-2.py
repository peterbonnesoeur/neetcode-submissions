class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
            The idea resolve around a set.

            We want to find elements that follow one another by adding
            1 to them.
            Thus we need only tp find starting points to make this work.
                ex: if we have [ 2, 3, 4], if we pick 2 as starting point, the length is 
                3 while if we pick 3, the length of the following element is 2.

                Thus, we can create a set, go over the array once, check if num -1 is in the set. 
                If not, add it to the candidates.
                Once the candidates are found, we can iterate in our set and count the max 
                amount of iteration needed to be put compute the max by iteratively checking
                if num + 1 is in the set
        """
        nums_set : set[int] = set(nums)
        max_length: int = 0

        for num in nums:
            if num-1 not in nums_set:
                length = 1
                while num + length in nums_set:
                    length += 1
                max_length = max(max_length, length)

        return max_length        