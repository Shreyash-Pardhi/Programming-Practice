'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
'''
def searchInsert(self, nums: List[int], target: int) -> int:
        # pos=0
        # i=0
        # if target in nums:
        #     pos = nums.index(target)
        # else:
        #     while i<=len(nums)-1 and nums[i]<target:
        #         pos+=1
        #         i+=1

        # return pos

        i=0
        while(i<len(nums)):
            if nums[i]==target or nums[i]>target:
                return i
            i+=1
        
        return i