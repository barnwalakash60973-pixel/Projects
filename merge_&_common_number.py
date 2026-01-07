def merge_all_elements(arr1, arr2):
  #Merge all elements from the both arrays

    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    arr = [0] *(n)

    for i in range(n1):
        arr[i] = arr1[i]

    for j in range(n2):
        arr[n1 + j] = arr2[j]

    return arr  

#======================================================================
  
def merge_different_elements(arr1, arr2):
    #Merge different elements from both arrays

    arr = []

    for i in arr1:
        arr.append(i)

    for j in arr2:
        if not j in arr:
            arr.append(j)
    

    return arr

#===============================================================

def merge_common_elements(arr1, arr2):
    #Merge only common elements from the array


    arr = []
    for i in arr1:
        if i in arr2:
            arr.append(i)


    return arr
    
arr1 = [2,0,8,-3,6,-4,1]
arr2 = [9,2,0,1,7,6]


result1 = merge_all_elements(arr1, arr2)
print("After merge arrays are: ",result1)

result2 = merge_different_elements(arr1, arr2)
print("After Merge only different elements: ",result2)

result3 = merge_common_elements(arr1, arr2)
print("After merge only common elements: ",result3)
