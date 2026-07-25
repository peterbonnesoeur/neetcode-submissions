class Solution:
    def change(self, amount: int, coins: List[int]) -> int:


        coins.sort()

        dp: dict[tuple[int], int] = dict()

        def dfs(target: int, i:int) -> int:
            """
                Go through the decision tree and try each coin to see if we
                Can reach the targeted amount
            """
            if target < 0 or i >= len(coins):
                return 0

            if target == 0: # Also handles the case where amount is 0
                return 1

            if (target, i) in dp:
                return dp[(target, i)]

            res = 0
            if target >= coins[i]:
                res = dfs(target, i+1)
                res += dfs(target - coins[i], i)
            
            dp[(target, i)] = res
            return res
        
            # able_to_go_to_target = 0
            # for i,coin in enumerate(coins):
            #     if i >= ignore_index:
            #         able_to_go_to_target += dfs(target - coin, i)
            # dp[(target, ignore_index)] = able_to_go_to_target
            # return able_to_go_to_target 

        amount = dfs(amount, 0)
        return amount