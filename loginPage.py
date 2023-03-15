import time
import random 

class Login:
    
    #class variable that stores all login data of different accounts
    loginDatabase = {}

    def __init__(self):
        #Creates an account for a new user
        print("\n----------------------------------------------------")
        print("SIGNUP")
        print("----------------------------------------------------\n")
        self.username = input("Enter Username: ")

        #Verifies if username is taken or not
        while self.username in Login.loginDatabase:
            print("\nUsername is taken\n")
            self.username = input("Enter Username: ")
        
        self.password = input("Enter Password: ")
        self.passwordC = input("Confirm Password: ")

        while self.password != self.passwordC:
            print("\nPasswords Do Not Match\n")
            self.password = input("Re-enter Password: ")
            self.passwordC = input("Confirm Password: ")

        #Provides an integer key to confirm identity if a user wants to change their password later
        self.recoveryKey = str(random.randint(0, 1000000000000))
        Login.loginDatabase[self.username] = (self.password, self.recoveryKey)

        print("Your recovery key to change your password: " + self.recoveryKey)
        time.sleep(1)

    def __str__(self):
        return "ELEVATE 1.0: Login Class for Property Manager"
    
    def menu(self):
        print("\n----------------------------------------------------")
        print("LOGIN PAGE")
        print("----------------------------------------------------\n")
        print("0 for Login")
        print("1 for Forget Password\n")

        loginNum = input("Enter option (0 or 1): ")

        while loginNum != "0" and loginNum != "1":
            print("\nInvalid Entry\n")
            loginNum = input("Enter option (0 or 1): ")

        time.sleep(1)

        if loginNum == "0":
            self.login()
        else:
            self.forgotPassword()

    def login(self):
        print("\n----------------------------------------------------")
        print("LOGIN")
        print("----------------------------------------------------\n")
    
        success = True
        attempt = 3

        #User has 3 attempts to correctly input their username and password 
        while (attempt > 0 or success):
            userAttempt = input("Username: ")
            passAttempt = input("Password: ")

            if self.username == userAttempt and self.password == passAttempt:
                time.sleep(1)
                print("\nLogin was sucessful\n")
                return True
            else:
                success = False
                attempt = attempt - 1
                print("Wrong username or password, " + str(attempt) + " more attempts\n")
        
        time.sleep(1)
        print("\nMaxed Login Attempts. Login Failure.\n")
        return False
    
    def forgotPassword(self):
        print("\n----------------------------------------------------")
        print("FORGOT PASSWORD")
        print("----------------------------------------------------\n")

        recoveryKey = input("Enter Recovery Key: ")

        #Checks if the recovery key is valid 
        while self.recoveryKey != recoveryKey:
            print("\nInvalid Recovery Key\n")
            recoveryKey = input("Enter Recovery Key: ")

        self.password = input("Enter New Password: ")
        self.passwordC = input("Confirm New Password: ")
    
        while self.password != self.passwordC:
            print("\nPasswords Do Not Match\n")

            self.password = input("Re-enter Password: ")
            self.passwordC = input("Confirm Password: ")

        #Provides user with a new recovery key
        self.recoveryKey = str(random.randint(0, 1000000000000))
        Login.loginDatabase.update({self.username: (self.password, self.recoveryKey)})

        time.sleep(1)
        print("\nPassword was changed succesfully.")
        print("Your new recovery key to change your password: " + self.recoveryKey + "\n")
        
pm = Login()
pm.menu()