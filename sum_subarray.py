def sumSubarray(nums):
    result = 0

    n = len(nums)

    for i in range(n):
        temp = 0
        for j in range(i,n):

            temp += nums[j]
            result += temp
    return result

nums = [1,2,3,4]
res = sumSubarray(nums)
print(res)                  #output -> 50

#Time complexity -> O(n^2)

#==================================================================

#optimal solution
def subarray_sum(nums):
    result = 0
    n = len(nums)

    for i in range(n):
        result += nums[i] * (i+1) * (n-i)

    return result

nums = [1,2,3,4]
res = subarray_sum(nums)
print(res)                     #output -> 50

#Time complexity -> O(n)