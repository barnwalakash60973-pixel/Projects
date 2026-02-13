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
            pass
        elif user_input == "2":
            pass
        elif user_input == "3":
            pass
        elif user_input == "4":
            pass
        else:
            exit()
        

app = chatbook()