class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        """
            Return the minimum number of coins for the amount
            In case it is impossible, return -1

            Coins are > 1 and amount > 0

            We can probably reason about this using a dp structure.


            Let's first write the dfs problem for this to see how we can make it work
        """

        # now, let's make it efficient

        dp: dict[int, int] = {}
        def dfs(target: int) -> int:
            """
                Go through the decision tree and try each coin to see if we
                Can reach the targeted amount
            """
            if target < 0:
                return float("infinity")

            if target == 0: # Also handles the case where amount is 0
                return 0

            if target in dp:
                return dp[target]
            
            min_amount_coins = float("infinity")
            for coin in coins:
                min_amount_coins = min(min_amount_coins, 1 + dfs(target - coin))
            dp[target] = min_amount_coins
            return min_amount_coins 

        amount = dfs(amount)
        return amount if amount != float("infinity") else -1
