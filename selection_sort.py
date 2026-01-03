#sort the array through selection sort
def selection_sort(arr):
    if not arr:
        return None
    
    for i in range(len(arr)):
        index = i

        for j in range(i+1, len(arr)):
            if(arr[index] > arr[j]):
                index = j

        arr[i],arr[index] = arr[index],arr[i]   #replace number

    return arr

arr = [7,2,-8,0,6,-1]

result = selection_sort(arr)
print("After sort the array is: ",arr)


