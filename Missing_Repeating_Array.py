'''
find missing and repeating number in an array.
'''


def find_missing_and_repeating(nums):
    n = len(nums)
    ms=None
    rn=None
    for i in range (n):
        if i<n-1 and nums[i]==nums[i+1]:
            rn=nums[i]
            nums.remove(nums[i])
            n-=1
            
    if(nums[0]!=1):
        ms=1
    else:
        for i in range(len(nums)):
            if nums[i]!=i+1:
                ms=i+1
                break
    return ms,rn

# Example usage
sorted_array = [1,2,2,3,5]
missing, repeating = find_missing_and_repeating(sorted_array)
print("Missing Number:", missing)
print("Repeating Number:", repeating
