def sort(arr):
# sort the array
    for i in range(len(arr) - 1):
        swap = False

        for j in range(len(arr) - i - 1):
            if(arr[j] > arr[j+1]):
                arr[j],arr[j+1] = arr[j+1],arr[j]    #replace number
                swap = True
        
        if not swap:
            break

    return arr


arr = [4,0,-3,8,-6,7]
result = sort(arr)
print("After sort the arrays: ",arr)