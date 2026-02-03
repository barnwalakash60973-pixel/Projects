"""Find the Missing Number

Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
This array represents a permutation of the integers from 1 to n with one element missing.
Find the missing element in the array.

Examples: 

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: Here the size of the array is 4, so the range will be [1, 5]. The missing number between 1 to 5 is 4

Try it on GfG Practice"""


# Code one the basis of above problem
#Approach 1 -> Brute Force
#Time Complexity -> O(n^2)

def index_in_array(nums):
    n = len(nums)

    for i in range(n):
        ind = i+1
        if ind not in nums:
            return ind
    
    return -1

nums = [1,2,5,4]
res = index_in_array(nums)
print(res)                             # Output -> 3

#====================================================================

def index_check_array(nums):
    n = len(nums)
    total = int(((n+2)*(n+1))/2)
    sum_arr = 0
    for i in range(n):
        sum_arr += nums[i]
    
    index = total - sum_arr

    return index

nums = [1,2,4,5]
result = index_check_array(nums)
print(result)                           

#Time complexity -> O(n)

