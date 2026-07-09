class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        curr_prefix = {0:-1} # remainder -> first index (virtual index before start)
        curr_sum = 0

        for i, num in enumerate(nums):
            curr_sum += num
            residual = curr_sum % k

            if residual in curr_prefix:# and curr_sum >= k:
                print(residual, curr_prefix, i - curr_prefix[residual])
                if i - curr_prefix[residual] > 1:
                    return True
                # print(residual, curr_prefix)
                # return
            else:
                curr_prefix[residual] = i
            

        return False