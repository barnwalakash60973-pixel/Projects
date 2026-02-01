def binarySearch(arr,tar):

    n = len(arr)
    for i in range(n):
        if arr[i] == tar:
            return i
    

arr = [-1,2,3,0,9,4]
tar = 0
result  = binarySearch(arr,tar)
print(result)                      # output -> 3
# Time Complexity -> O(n)

#===========================================================

def rotated_binary_search(arr,tar):
    n = len(arr)
    st = 0
    end = n-1
    while(end >= st):

        mid = st + int((end - st)/2)
        if arr[mid] == tar:
            return mid

        if arr[st] <= arr[mid]:  #Left Sorted

            if (arr[st] <= tar and tar <= arr[mid]):
                end = mid - 1
            else:
                st = mid + 1

        elif arr[end] >= arr[mid]: # Right Sorted

            if (arr[mid] <= tar and tar <= arr[end]):
                st = mid + 1
            else:
                end = mid - 1
    return -1
nums = [1,2,3,4,5,0,1,2]
tar = 0
result = rotated_binary_search(nums,tar)
print(result)

#Time Complexity -> O(logn)

