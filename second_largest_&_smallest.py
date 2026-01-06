def second_largest(arr):
    # find second maximum number in the array

    if (len(arr) <= 2):     #if array has two elements return none
         return None

    largest = second_max = float('-inf')    #assume largest and second_max are -infinite
    
    for num in arr: 

        if(num > largest):
            second_max = largest
            largest = num

        elif num > second_max and second_max != largest:
                second_max = num


    return second_max




def second_smallest(arr):
    #find second minimum number in the array
     
    if (len(arr) <= 2):        #if array has two elements return none
          return None
    
    smallest = second_min = float('inf')         #assume smallest and second min are infinite 

    for num in arr:
        if num < smallest:
             second_min = smallest
             smallest = num
         
        elif num < second_min:
             second_min = num

    return second_min

arr = [-1,-3,-4,4,0,9,6,7]

max = second_largest(arr)
print("The second maximum number in the array is: ",max)

min = second_smallest(arr)
print("The second minimum number in the array is: ",min)
    