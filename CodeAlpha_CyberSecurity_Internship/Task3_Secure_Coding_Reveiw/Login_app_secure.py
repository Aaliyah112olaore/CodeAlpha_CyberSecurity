import hashlib
import os

# The "Database" of registered users:
users = {}


def thehash_password(password, salt=None):
    #Hash a password using SHA-256

    return hashlib.sha256(password.encode()).hexdigest()


# Create Register
def register():
    # Ask for a username
    username = input("Enter a username: ").strip()
    
    # Reject empty usernames
    if not username:
        print("Please insert a username.")
        return
    
    # Don't allow registering over an existing account
    if username in users:
        print("Registration could not be completed.")
        return
    
    while True:
        password = input("Enter a password: ")
    
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
        elif not any(char in "!@#$%^&*" for char in password):
            print("Password must contain at least one special character.")
        else:
            # If password is correct stop asking
            break

    # Store the hash password, never the plain

    users[username] = thehash_password(password)
    print("Registration sucessfully")


register()


# Create Login
def login():
    while True:
        # Ask for username first
        username = input("Enter your username: ")
        if username not in users:
            print("Invalid username. Please try again")
            continue
           
    # Allow only 3 password attempts
        attempts = 0
        max_attempts = 3
    
        while attempts < max_attempts:
             password = input("Enter your password: ")

             if users[username] == thehash_password(password):
                 print("Login Successful")
                 break
             else:
                 attempts += 1
                 print("Invalid password. Please try again.")

        # Once logged in, wait for the user to type logout
        while True:
            Logout = input("Enter your 'logout' to logout: ").lower()
            if Logout == "logout":
                print("You have successfuly logged out")
                break  # exit the logout loop
            else:
                print("Invalid password. Please try again")

        break  # <-- exit the OUTER (username) loop,

login()
