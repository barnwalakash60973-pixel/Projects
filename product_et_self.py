# Product the subarray except itself

def product_subarray(nums):
    n  = len(nums)
    prod = [1] * n

    for i in range(n):
        
        for j in range(n):
            if i != j:
                prod[i] *= nums[j]

    return prod

nums = [1,2,3,4] 
result = product_subarray(nums)
print(result)                   #output -> [24,12,8,6]

#Time complexity -> O(n^2)

#================================================================
#optimal approach same problem

def product_subarray(nums):
    n = len(nums)
    pre = [1] * n
    suf = [1] * n
    result = [0] * n

    for i in range(1,n):
        pre[i] *= pre[i-1] * nums[i-1]
    
    for j in range(n-2,-1,-1):
        suf[j] = suf[j+1] * nums[j+1]

    for i in range(n):
        result[i] = pre[i]*suf[i]

    return result

nums = [1,2,3,4]
res = product_subarray(nums)
print(res)                      #output -> [24, 12, 8, 6]

#Time complexity -> O(n)
        