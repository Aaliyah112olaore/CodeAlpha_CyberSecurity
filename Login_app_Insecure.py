users={}

def register():
    username=input("Enter a username: ")
    password=input("Enter a password: ")

    users[username]=password
    print("Registration successful!")

def login():
    username=input("Enter your username: ")
    password=input("Enter your password: ")

    if username in users and users[username]==password:
        print("Login succesful!")
    else:
        print("Invalid username or password. ")

while True:
    print("\n---Login System---")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")




        
    
