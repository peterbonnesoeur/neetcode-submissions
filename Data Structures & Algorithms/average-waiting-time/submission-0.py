class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        waiting_time : int = 0
        end_time : int = 0

        for start_time, prep_time in customers:
            if end_time <= start_time:
                end_time = start_time + prep_time
                waiting_time += prep_time
            else:
                # Consider the delay in prep
                waiting_time += end_time - start_time + prep_time
                # Append the prep time to the existing end time
                end_time += prep_time

        return waiting_time / len(customers)