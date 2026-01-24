#Simple version to right shift elements
def right_shift(nums,d):

    n = len(nums)

    for i in range(d):
        num = nums[n-1]

        for j in range(n-1,0,-1):
            nums[j] = nums[j-1]
        nums[0] = num

    return nums
nums = [7,8,5,0]


d=2
print(right_shift(nums,d))

#Time complexity -> O(n*d)

#================================================================


#Right shift elements best approach
def right_shift(nums,d):
    n = len(nums)
    temp = [0]*n
    for i in range(d):
        temp[i] = nums[n-d+i]

    for i in range(n-d):
        temp[d+i] = nums[i]

    for i in range(n):
        nums[i] = temp[i]
    return nums
nums = [0,3,4,5,6]
d = 3
result = right_shift(nums,d)
print(result)