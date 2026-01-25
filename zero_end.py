#Last side shift all zero elements
def zero_shift_right(nums):
    
    list = []

    for i in range(len(nums)):
        if nums[i] != 0:
            list.append(nums[i])
    
    for i in range(len(nums)):
        if nums[i] == 0:
            list.append(nums[i])
    
    return list


nums = [1,2,0,0,5]
result = zero_shift_right(nums)
print(result)                   #output -> [1,2,5,0,0]
#============================================================

#NO use other list
def list_sended_zero(nums):
    count = 0
    
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[count] = nums[i]
            count += 1
    
    while count < len(nums):
        nums[count] = 0
        count += 1
    
    return nums

nums = [1,0,3,0,0,8]
results = list_sended_zero(nums)
print(results)                      #output -> [1, 3, 8, 0, 0, 0]



#=============================================================
#Fast approch through swap 

def last_shift_arr(nums):
    count = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[count] = nums[count],nums[i]
            count += 1
    
    return nums
nums = [1,0,0,3,-2,0,9]
res = last_shift_arr(nums)
print(res)                    #output -> [1,3,-2,9,0,0,0]

