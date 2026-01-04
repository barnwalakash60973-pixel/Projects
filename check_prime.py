def check_prime_number(nums):

    if (nums <= 1):
        print("No prime number exist")

    
    else:
        print("The prime numbers are:")
        for i in range(2, nums+1):

            check = False  #assume all is prime

            for j in range(2, (i//2 + 1)):
                if (i % j == 0):
                    check = True
                    break
        
            if (check == False):
                print(i)

nums = 30
check_prime_number(nums)
