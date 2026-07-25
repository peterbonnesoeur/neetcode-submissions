class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        """
            Return the minimum amount of dollars spent during the trip

            So this will be a conditional dfs where the condition will influence the time skip

            the days are always sorted
            costs always of length 3 and cost is always >=1

            We assume that when we buy an additional pass, it means that 
            the past one is expired -> we jump to the next dat
        """

        max_day = days[-1]

        dp : dict[int, int] = {}
        def dfs(day: int):
            # print(day)
            if day >= max_day:
                return 0

            if day in dp:
                return dp[day]

            curr_index = 0

            while days[curr_index] <= day and curr_index < (len(days)):
                curr_index += 1

            # we remove 1 to all as it includes the current day...
            ticket_1_day = costs[0] + dfs(days[curr_index] + 1 - 1)
            ticket_7_day = costs[1] + dfs(days[curr_index] + 7 - 1)
            ticket_30_day = costs[2] + dfs(days[curr_index] + 30 - 1)
            dp[day] = min(ticket_1_day, ticket_7_day, ticket_30_day)
            # res = ticket_30_day

            return dp[day]

        return dfs(0)
            