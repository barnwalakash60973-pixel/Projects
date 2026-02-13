class chatbook:
    def __init__(self):
        self.username = ""
        self.password = ""
        self.login = False
        self.menu()

    # =====================Start the application process=====================
    def menu(self):
        print("_____________________________Welcome Sir/Mam____________________________")
        print()
        user_input = input("""Welcome to the Chatbook-How would you like to proceed?
                           1. Press 1 for signup
                           2. Press 2 for Signin
                           3. press 3 to write a post
                           4. Press 4 to send message a friend
                           5. Press any other key for exit: """)
        
        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.post_message()
        elif user_input == "4":
            self.send_message_friend()
        else:
            exit()

     #=======================For Signup code==========================    
    def signup(self):
        email = input('Enter your email:')
        password = input('Enter your password:')
        self.username = email
        self.password__ = password
        print('You have signup succesfully.')
        print("\n")
        self.menu()
    
    #=========================For login website code======================
    def signin(self):

        if self.username == "" and self.password == "":
            print("Please signup!")
            self.menu()


        else:
            username = input("Enter your username/email: ")
            password = input("Enter your password: ")

            if self.username == username and self.password == password:
                print("Succesfully Sigin...")
                self.login = True
                self.menu()

            else:
                print("Please enter correct username and password...")
                self.menu()
    
    #===========================For post meessage code====================
    def post_message(self):

        if self.login == True:
            txt = input("Enter your post: ")
            print("Post Succesfully...")
            self.menu()

        else:
            print("Please you need to login first!")
            self.menu()
    
    #======================Code For Send Message to Friend==================
    def send_message_friend(self):

        if self.login == True:
            txt = input("Enter your message: ")
            print("Successfully send message to your friend...")
            self.menu()

        else:
            print("You Need To Login!")
            self.menu()

    #=========================Exit website code===========================
    def exit(self):
        print("Thanks for using.")

        print("Come Soon Again!")

        print("_________________________God Bless You________________________________")
        
app = chatbook()