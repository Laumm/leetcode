class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2) :
            nums1,nums2 = nums2,nums1
        ib = 0
        ie = len(nums1) 
        while True :
            i =  (ib +ie) // 2
            j = (len(nums1) + len(nums2) + 1) //2 - i
            if  i > 0 and  nums1[i-1] > nums2[j]:
                ie = i
                continue
            if   i < len(nums1) and  nums2[j-1] > nums1[i] :
                ib = i+1
                continue
            total =len(nums1 )+len( nums2) 
            if total % 2 == 0 :
                return (max(nums1[0:i] + nums2[0:j]) + min(nums1[i:]+nums2[j:])) /2
            else :
                return max(nums1[0:i] + nums2[0:j])
