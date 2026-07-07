class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        
        if len(nums) == 1:
            return True
        
        is_past_odd = nums[0] % 2
        for i in range(1, len(nums)):
            is_current_odd = nums[i]%2
            if is_past_odd and is_current_odd == 1:
                return False
            
            if not is_past_odd and is_current_odd == 0:
                return False

            is_past_odd = is_current_odd

        return True