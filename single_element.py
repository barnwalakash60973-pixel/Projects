#find single number in arrray

#Through Brute force approch

def single_elemnet_array(arr):

    n = len(arr)
    
    for i in range(n):
        num = arr[i]
        if arr.count(num)==1:
            return num
    return -1

nums = [1,2,3,1,2]
res = single_elemnet_array(nums)
print(res)                         #output -> 3

#Time Complexity -> O(n)

#======================================================================

#same code by optimum aproach

def single_number_array(arr):
    n = len(arr)
    num = 0
    for i in range(n):
        num ^= arr[i]

    return num

arr = [1,3,2,2,1] 
result = single_number_array(arr)
print(result)                      #output -> 3
#Time complexity -> O(n)