from cryptography.fernet import Fernet
import os
import sys

def main():
    username = input("Enter your username: ")
    username_path = f"files/{username}_key.txt"
    
    #checking if the user exists
    if os.path.exists(username_path):
        print(f"Welcome back {username}")
    
    else:
        print("Creating user...")
        key = Fernet.generate_key()
        
        with open(username_path, "w") as file:
            file.write(f"{key}")
            print(f"User {username} has been created")
            
    fernet = Fernet(key)
    
    while True:
        print("Do you want to 'Save', 'View' or 'Exit'", end="")
        choice = input().lower()
        
        if choice == "save":
            save(fernet, username)
            break
        elif choice == "view":
            view(fernet, username)
            break
        elif choice == "exit":
            sys.exit()
            
            
def save(fernet, username):
    user_path = f"files/{username}_data.txt"
    
    platform_name = input("Enter the platform name: ")
    account_username = input("Enter your username: ")
    account_password = input("Enter your password: ")
    
    with open(user_path, "w") as file:
        file.write(f"{platform_name} | {account_username}, {account_password}\n")
        print(f"Data has been saved for {platform_name}")
    
    
def view(fernet, username):
    user_path = f"files/{username}_data.txt"
    
    with open(user_path, "r") as file:
        

    
if __name__ == "__main__":
    main()