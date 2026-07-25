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

        total = sum(stones)
        half = total // 2
        # checklist = [False] * (half + 1) # checklist[i] = can you have weight i with stones you have
        # checklist[0] = True # 0 weight can be achieved by picking nothing
        checklist = set() # 0 weight can be achieved by picking nothing
        checklist.add(0)
        for stone in stones:
            for j in range(half, stone - 1, -1):
                if (j - stone) in checklist:
                    checklist.add(j)
        for j in range(half, -1, -1):
            if j in checklist:
                return total - 2*j



        # stone_sum = sum(stones)
        # target = math.ceil(stone_sum / 2)
        # dp: dict[tuple[int], int] = dict()

        # # Better but not quite... There must be a better/smarter way of caching thing...

        # # the length of the resting stones? No, the exact combination of stones could be useful

        # def dfs(i: int, total: int):
            
        #     if i == len(stones):
        #         return abs(total - (stone_sum - total))
            
        #     if (i, total) in dp:
        #         return dp[(i, total)]

        #     dp[(i, total)] = min(dfs(i+1, total), dfs(i+1, total + stones[i]))

        #     return dp[(i, total)]

        # return dfs(0, 0)