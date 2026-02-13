class Calculator:
    def __init__(self, num):
        self.num = num
    

    def calculate(self):
         if self.num == 1:
             self.sum(4, 8)
         elif self.num == 2:
             self.product(6, 7)
         else:
            print('invalid')

    def sum(self, num1, num2):
        print(num1 + num2)

   
    def product(self, num1, num2):
        print(num1 * num2)



num = int(input('Enter a number: '))
cal = Calculator(num)
cal.calculate()


#==============================================================================

class Car:
    def __init__(self, car, color, purchase):
        self.car = car
        self.color = color
        self.purchase = purchase

    def car_details(self):
        return f"Car name:{self.car}, color:{self.color} and purchase:{self.purchase}"

c = Car('Royato', 'Black',1230000)
c1 = c.car_details()
print("car details: ",c1)
        
        
#=========================================================================================
class Password_Game:
    def __init__(self, password):
        self.password = password
    def menu(self):
        print('Welcome to password game:')
        while True:
            print('1 -> password change')
            print('2 -> Exit')
    
            num = int(input('Enter the number'))
        
            if num == 1:
                self.change_password()

            elif num == 2:
                self.exit()

            else:
                print('Please enter a number must be 1 or 2')
        
    def change_password(self):
        old_pass = input('Enter the password: ')
        if self.password == old_pass:
            new_pass = input('Enter the new password: ')
            self.password = new_pass
            print('password change succesfully')
        else:
            print('Please enter the correct password.')
    def exit(self):
        exit()


p = Password_Game('akash123')
p.menu()