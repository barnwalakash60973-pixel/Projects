"""Stock Buy and Sell - Multiple Transaction Allowed

Given an array prices[] representing stock prices, find the maximum total profit that can be earned by buying and selling the stock any number of times.

Note: We can only sell a stock which we have bought earlier and we cannot hold multiple stocks on any day.

Examples:

Input: prices[] = [100, 180, 260, 310, 40, 535, 695]
Output: 865
Explanation: Buy the stock on day 0 and sell it on day 3 = 310 - 100 = 210 and Buy the stock on day 4 and sell it on day 6 = 695 - 40 = 655 so the Maximum Profit  is = 210 + 655 = 865.
"""


#this code on the basis of above problem
#Time complexity -> O(n)

def max_profit(stock):
    n = len(stock)
    max_profit = 0
    profit = 0

    for i in range(1,n):
        if stock[i] > stock[i-1]:
            profit = stock[i] - stock[i-1]
            max_profit += profit
    
    return max_profit

stock = [100,180,260,310,40,590,610]
result = max_profit(stock)
print(result)                                 #output -> 780

#======================================================================


#find pick index  in Mountain array (Given array must in incresing and decreasing order)

def mountain_pick(nums):
    end = len(nums) - 2
    st = 1

    while(st <= end):
        mid = st + int((end-st)/2)
        
        if nums[mid-1] < nums[mid] and nums[mid] > nums[mid+1]:
            return mid
        
        if nums[mid-1] < nums[mid]:
            st = mid + 1
        else:
            end = mid-1


    return -1

nums = [1,2,3,4,9,5,3,0]
result = mountain_pick(nums)
print(result)
 