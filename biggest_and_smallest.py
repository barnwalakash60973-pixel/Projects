def biggest_num(arr):
    #find biggest number in array

    max = arr[0]
    for num in arr:
        if(num > max):
            max = num

    return max

def smallest_num(arr):
    #find smallest number in array

    min = arr[0]
    for num in arr:
        if(num < min):
            min = num

    return min

arr = [-2,3,9,0,5,6,-7]

if not arr:   #check array if empty
    print("The array is empty")
else:
    big = biggest_num(arr)
    print("The biggest number in the array is: ",big)

    small = smallest_num(arr)
    print("The smallest number in the array is: ",small)