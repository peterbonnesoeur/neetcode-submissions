class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tab = 0
        for i in range(len(nums1)):
            if tab >=n:
                continue

            if i >= (len(nums1) - n):
                nums1[i] = nums2[tab]
                tab += 1
            elif nums2[tab] <= nums1[i]:
                nums1[i], nums2[tab] = nums2[tab], nums1[i]
                offset = 0
                while (tab+offset + 1) < n and nums2[tab+offset] > nums2[tab+offset + 1]:
                    nums2[tab+offset + 1], nums2[tab+offset] = nums2[tab+offset], nums2[tab+offset + 1]
                    offset += 1
        