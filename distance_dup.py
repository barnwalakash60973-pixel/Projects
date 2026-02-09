# -> Duplicate within K Distance in an Array
def dup_dist_element(nums, k):
    n = len(nums)
    
    for i in range(n):
        for j in range(i+1, k+1):
            if ((nums[i] == nums[j]) and abs(i-j) <= k):
                return True
                
                

    
    return False

nums = [1,2,3,1,7,0]
k = 4
result = dup_dist_element(nums,k) 
print(result)
#Time Complexity -> O(n)


#==================================================================                
#Missing and Repeating in an Array



from collections import Counter
def missing_repeat_element(nums):
    n = len(nums)
    counts = Counter(nums)               #count the each element
    missing_repeat = []
    for i in range(n-1,-1,-1):
        if counts[nums[i]] > 1:
            missing_repeat.append(nums[i])
            counts[nums[i]] -= 1           #it's sure one duplicate remove.
            nums.pop(i)

    total = sum(nums)            #calculate sum after remove duplicate elemets
    
    n1 = len(nums)
    total_sum = (n1+1)*(n1+2)//2

    missing_repeat.append(total_sum-total)
    return missing_repeat



nums = [1,3,1]
result = missing_repeat_element(nums)
print(result)

#Time Complexity -> O(n)