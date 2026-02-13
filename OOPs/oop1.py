class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False
        self.menu()

    def menu(self):
        user_input = input("""Welcome to the Chatbook-How would you like to proceed?
                           1. Press 1 for signup
                           2. Press 2 for Signin
                           3. press 3 to write a post
                           4. Press 4 to send message a friend
                           5. Press any other key for exit.""")
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        
    def signup(self):
        email = input('Enter your email:')
        password = input('Enter your password:')
        self.username = email
        self.password = password
        print('You have signup succesfully.')
        print("\n")
        self.menu()
    

    def signin(self):
        if self.username == "" and self.password == "":
            print("Please signup!")
            self.menu()
        else:
            username = input("Enter your username/email: ")
            password = input("Enter your password: ")
            if self.username == username and self.password == password:
                print("Succesfully sigin")
                self.login = True
                self.menu()
            else:
                print("Please enter correct username and password!")
                self.menu()
    

app = chatbook()