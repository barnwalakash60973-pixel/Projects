def sort(arr):
    maximum = max(arr)
    
    elements = [0] * (maximum + 1)
    for i in arr:
        elements[i] += 1

    list = []

    for num in range(len(elements)):
        list.extend(elements[num] * [num])

    return list

arr = [8,4,3,4,1,4,2,1,1,2]
result = sort(arr)
print("The sort after the array:",result)