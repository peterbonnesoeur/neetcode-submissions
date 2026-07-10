class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            The median has the following property:
                if the array is odd: pos = len(array) // 2 (ex: array of 3 element -> index 1)
                if the array is even: pos = (len(array)//2 + len(array)//2  +1 )/2

            Now, both arrays are sortedso my assumption is to have 2 pointers set at the virtual median point of both arrays

            total_length = len(nums1) + len(nums2)

            the goal is to find a binding relationship between one and the other.
            we want to iterate on the smaller array and relates the other pointer's
            position as a relative position.


            l_a, r_a = len(array)//2, len(array)//2 -1
            l_b, r_b = total_length//2 - l_a, total_lenght//2 - r_a

            conditions:

            if v_l_a <= v_r_b and v_r_a >= v_l_b:
                Goal -> we get the median
                if array is pair:
                    max(v_l_a, v_l_b) + min(v_r_a, v_r_b)
                if array is odd:
                    min(v_r_a, v_r_b)
            if v_l_a <= v_r_b:
                l_a +=1 
                r_a +=1
        """

        # It is a binary search...

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total//2
        if len(A)> len(B):
            A,B = B, A
        
        l, r = 0, len(A) - 1
        while True:

            i = (r+l) // 2
            j =  half - i -2
            #deeply understand the - 2

            Aleft = A[i] if i>=0 else -float("infinity")
            Aright = A[i+1] if i+1 < len(A) else float("infinity")
            Bleft = B[j] if j>= 0 else -float("infinity")
            Bright = B[j+1] if j+1 < len(B) else float("infinity")

            if Aleft <= Bright and Aright >= Bleft:
                if total%2:
                    return min(Bright, Aright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            elif Aleft > Bright:
                r = i-1
            else: # Bleft> Aright
                l = i+1
        