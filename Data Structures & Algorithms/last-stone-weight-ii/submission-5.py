class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        """
            We want here to remember the smallest weight of the resulting stone
            clashes that we can achieve.

            That weight can also be 0

            seems like a dfs style of problem, were we pick a stone a vs a stone b
            the question is how to start it?

            Shall we pick a stone at random?

            I think that we shall choose to use the stone or not

            Let's first do a defs based solution before thinking about how we can cache 
            some subresults:

        """

        # Now, how do we cache the state?
        # What do we really care about?


        stone_sum = sum(stones)
        target = math.ceil(stone_sum / 2)
        dp: dict[tuple[int], int] = dict()

        # Better but not quite... There must be a better/smarter way of caching thing...

        # the length of the resting stones? No, the exact combination of stones could be useful

        def dfs(i: int, total: int):
            
            if i == len(stones):
                return abs(total - (stone_sum - total))
            
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))

            return dp[(i, total)]

        return dfs(0, 0)