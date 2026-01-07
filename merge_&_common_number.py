def merge_all_elements(arr1, arr2):
    #Merge both arrays with all elements
    
    n1 = len(arr1)
    n2 = len(arr2)
    n = n1 + n2
    arr = [0] * (n)

    for i in range(n1):
        arr[i] = arr1[i]
    
    for j in range(n2):
        arr[n1+j] = arr2[j]
    return arr
#========================================================================
def merge_different_elelments(arr1, arr2):
    #Merge only those elements which is not common in both arrays

    arr = []

    for i in arr1:
        arr.append(i)

    for j in arr2:
        if not j in arr:                 #check if element not in arr2
              arr.append(j)

    return arr
#========================================================================

def merge_common_elements(arr1, arr2):
    #Merge only common elements from the arrays

    arr = []

    for i in arr1:
        if i in arr2:                      #check element in arr2 
            arr.append(i)

    return arr
#===========================================================================    

arr1 = [2,0,9,-1,3,7,8]
arr2 = [-3,7,3,8,0]

result1 = merge_all_elements(arr1, arr2)
print("The merge all elements from the both arrays: ",result1)

result2 = merge_different_elelments(arr1, arr2)
print("The merge only different elements from the both arrays: ",result2)

result3 = merge_common_elements(arr1, arr2)
print("The merge only common elelments from the both arrays: ",result3)