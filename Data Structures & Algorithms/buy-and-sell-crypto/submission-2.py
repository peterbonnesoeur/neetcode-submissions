class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) == 0:
            return 0

        # read the text before...
        # we only do 1 transcation. we need to remember the last min of our window and the bigger max...
        
        curr_min = prices[0]
        max_return = 0
        for i in range(1, len(prices)):
            # if prices[i-1] < prices[i]:
            max_return  =  max(prices[i] - curr_min, max_return)
                # curr_min = prices[i]
            # else:
            curr_min = min(prices[i], curr_min)

        return max_return
        