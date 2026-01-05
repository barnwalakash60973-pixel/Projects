#Remove duplicates elements from arrys.
def remove_elements(arr):

    if not arr:
        print('Array is empty.Please enter the elements!')

    else:

        array = []

        for i in arr:
            if i not in array:   #check elements if not array then next process else no next process
               array.append(i)

        return array


arr = [1,0,-3,1,0,4,0]

result = remove_elements(arr)
print("The array after remove the duplicates element: ",result)

#======================================================================#



#Sum of all array elements 
def sum_of_elements(arr):

    if not arr:
        print("Arrays is empty.Please enter the elements!")

    else:
        sum = 0
        priduct = 1
        for num in arr:
            sum += num
           

        return sum
    
        
arr = [1,-3,5,-4,9]
result = sum_of_elements(arr)
print("The sum  of each elements are: ",result)

#==================================================================#

#Products of each array elements
def product_of_elements(arr):

    if not arr:
        print("Arrays is empty.Please enter the elements!")

    else:
        
        product = 1
        for num in arr:
            product *= num
           

        return product
    
        
arr = [1,-3,5,9]
result = product_of_elements(arr)
print("The product of each elements are: ",result)

    
#===================================================================#        

