class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) >= len(nums2):
            temp1 = nums1
            temp2 = nums2
        else:
            temp1 = nums2
            temp2 = nums1
            nums1 = temp1
            nums2 = temp2
            
        if len(temp2):
            pass
        else:
            if len(temp1) == 1:
                return temp1[0]
            else:
                return (temp1[len(temp1) / 2] + temp1[(len(temp1) - 1) / 2]) / 2.0
            
        while 1:
            if len(temp2) == 1 and len(temp1) == 1:
                return (temp1[0] + temp2[0]) / 2.0
            
            elif len(temp2) == 1 and len(temp1) > 1:
                if len(temp1) % 2 == 0:
                    more1 = temp1[len(temp1) / 2]
                    less1 = temp1[(len(temp1) - 1) / 2]
                    if temp2[0] >= more1:
                        return more1
                    elif temp2[0] <= less1:
                        return less1
                    else:
                        return temp2[0]
                    
                else:
                    more1 = temp1[(len(temp1) / 2) + 1]
                    median1 = temp1[len(temp1) / 2]
                    less1 = temp1[(len(temp1) / 2) - 1]
                    if temp2[0] >= more1:
                        return (more1 + median1) / 2.0
                    elif temp2[0] <= less1:
                        return (less1 + median1) / 2.0
                    else:
                        return (median1 + temp2[0]) / 2.0
                
            else:
                if len(temp1) % 2 == 1 and len(temp2) % 2 == 1:
                    median1 = temp1[len(temp1) / 2]
                    median2 = temp2[len(temp2) / 2]
                    if median1 == median2:
                        return median1
                    elif median1 < median2:
                        _ = len(temp2)
                        temp2 = temp2[: ((len(temp2) / 2) + 1)]
                        temp1 = temp1[(_ - len(temp2)): ]
                    else:
                        _ = len(temp2)
                        temp2 = temp2[(len(temp2) / 2): ]
                        temp1 = temp1[: -(_ - len(temp2))]
                        
                elif len(temp1) % 2 == 0 and len(temp2) % 2 == 1:
                    more1 = temp1[len(temp1) / 2]
                    less1 = temp1[(len(temp1) - 1) / 2]
                    median2 = temp2[len(temp2) / 2]
                    if median2 >= less1 and median2 <= more1:
                        return median2
                    elif median2 > more1:
                        _ = len(temp2)
                        temp2 = temp2[: ((len(temp2) / 2) + 1)]
                        temp1 = temp1[(_ - len(temp2)): ]
                    else:
                        _ = len(temp2)
                        temp2 = temp2[(len(temp2) / 2): ]
                        temp1 = temp1[: -(_ - len(temp2))]
                        
                elif len(temp1) % 2 == 1 and len(temp2) % 2 == 0:
                    median1 = temp1[len(temp1) / 2]
                    more2 = temp2[len(temp2) / 2]
                    less2 = temp2[(len(temp2) - 1) / 2]
                    if median1 >= less2 and median1 <= more2:
                        return median1
                    elif median1 < less2:
                        _ = len(temp2)
                        temp2 = temp2[: (len(temp2) / 2)]
                        temp1 = temp1[(_ - len(temp2)): ]
                    else:
                        _ = len(temp2)
                        temp2 = temp2[(len(temp2) / 2): ]
                        temp1 = temp1[: -(_ - len(temp2))]
                        
                else:
                    more1 = temp1[len(temp1) / 2]
                    less1 = temp1[(len(temp1) - 1) / 2]
                    more2 = temp2[len(temp2) / 2]
                    less2 = temp2[(len(temp2) - 1) / 2]
                    if more1 <= less2:
                        _ = len(temp2)
                        temp2 = temp2[: (len(temp2) / 2)]
                        temp1 = temp1[(_ - len(temp2)): ]
                    elif more2 <= less1:
                        _ = len(temp2)
                        temp2 = temp2[(len(temp2) / 2): ]
                        temp1 = temp1[: -(_ - len(temp2))]
                    else:
                        if less1 >= less2 and less1 <= more2 and more2 <= more1:
                            return (less1 + more2) / 2.0
                        elif less1 <= less2 and less2 <= more1 and more1 <= more2:
                            return (less2 + more1) / 2.0
                        elif less1 <= less2 and more2 <= more1:
                            return (less2 + more2) / 2.0
                        else:
                            return (less1 + more1) / 2.0
