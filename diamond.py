def diamond_shape(nums):
    if (nums < 1):
        print('Diamond shape is not possible')
    
    else:
        for i in range(nums):

            space = nums - 1 - i
            for j in range(space):
                print(' ', end = '')
    
            upper = 2 * i + 1
            for j in range(upper):
                print('*', end = '')
    
            print()   #New line

        for i in range(nums - 1):
    
            lower_space = i+1
            for j in range(lower_space):
                print(' ', end = '')
    
            lower = (2 * (nums) - 1) - 2 * (i + 1) 
            for j in range(lower):
                print('*', end = '')
    
            print()  #New line


nums = 5
diamond_shape(nums)  