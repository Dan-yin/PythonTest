'''
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:
nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
'''

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sortednums = sorted(nums1+nums2)
            
        lensum = len(sortednums)
        if lensum % 2 == 1:
            return sortednums[int(lensum/2)]
        else:
            #lensum/2 四舍五入
            return (sortednums[int(lensum/2)]+sortednums[int(lensum/2)-1])/2

        