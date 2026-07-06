class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # if target in nums:
        #     return True
        # else:
        #     return False

        # to go as fast as possible, we can use a binary search to identify
        # the point were the target is within a subarray.

        # 1 - we determine a mid point
        # 2 - if l < mid -> array is sorted in the left side 
        #     (stricly inferior as we might have some repeated char)
        #   - if l <= target <=mid -> default to binary search
        # 3 = if l >= mid -> the rotation point is within the subarray [l:mid]
        #      ex: [4 5 1 2 3] -> where mid_val = 1 and l_val = 4    
        #      for target == 5 -> if target > l or target < mid -> keep binary on [ l: mid]
        #       mid_val = 5
        #      for target == 2 -> binary search (regular on [mid:r+1])


        # [ 0 1 2 3]
        # l = 0, r = 3
        # mid = 3/2 = 1.5
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (r + l)//2  # I forgot (l+r)//2
            if nums[mid] == target:  # always check the middle -> then we ALWAYS exclude it
                return True

            # Those below just scan the array -> bad
            # while nums[l] == nums[mid] and l<mid:
            #     l+=1
            # while nums[r] == nums[mid] and r>mid:
            #     r-=1
            if nums[l] == nums[mid] == nums[r]:
                r-=1
                l+=1
                continue
            
            # left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # right half is sorted
            else:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

           
            # elif nums[mid] <= nums[l]:
            #     if target < nums[mid]:
            #         while nums[l] >= nums[mid] and l <= mid :
            #             l += 1
            #     if target >= nums[l]:
            #         while nums[mid] < nums[l] and mid > l:
            #             mid -= 1
            #     r = mid - 1
            # elif nums[r] <= nums[mid]:
            #     if target >= nums[mid]:
            #         while nums[r] < nums[mid] and r > mid :
            #             r -= 1
            #     if target < nums[r]:
            #         while nums[mid] >= nums[l] and mid >= r:
            #             mid += 1

        return nums[r] == target or nums[l] == target
            