class Solution(object): #O((M+N) log(M+N)) HARD
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        new_list = nums1 + nums2
        new_list.sort()
        n = len(new_list)
        if (n % 2 == 0):
            median = float((new_list[(n/2)-1] + new_list[((n/2)+1)-1])) / 2
        else:
            median = float(new_list[((n+1)/2)-1])
            
        return median
        
