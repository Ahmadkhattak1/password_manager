from cryptography.fernet import Fernet
import os
import sys

def main():
    username = input("Enter your username: ")
    username_path = f"files/{username}_key.txt"
    
    
    #checking if the user exists
    if os.path.exists(username_path):
        print(f"Welcome back {username.capitalize()}!")
        
        with open(username_path, "r") as file:
            key = file.readline().encode()

    
    else:
        print("Creating user...")
        key = Fernet.generate_key()
        
        with open(username_path, "w") as file:
            file.write(f"{key.decode()}")
            print(f"User {username} has been created")
            
    fernet = Fernet(key)
    
    while True:
        print("Do you want to 'Save', 'View', 'More options' or 'Exit': ", end="")
        choice = input().lower()
        if choice == "save":
            save(fernet, username)
        elif choice == "view":
            view(fernet, username)
        elif choice == "more options":
            print(f"Delete or Update: ", end="")
            more_choice = input().lower()
            if more_choice == "delete":
                delete(username, fernet)
            elif more_choice == "update":
                update(username, fernet)   
        elif choice == "exit":
            sys.exit()
        
            
            
def save(fernet, username):
    user_path = f"files/{username}_data.txt"
    
    platform_name = input("Enter the platform name: ").capitalize()
    
    #Checking to see if there is one account already saved for the platform
    
    
    account_username = input("Enter your username: ")
    account_password = input("Enter your password: ")
    
    #Encrypting the data separately so I can decode with writing to the file (encoding is necessary for encryption)
    encrypted_name = fernet.encrypt(platform_name.encode())
    encrypted_username = fernet.encrypt(account_username.encode())
    encrypted_password = fernet.encrypt(account_password.encode())
    
    #Decoding the data when writing to the file because I will need to encode it when decrypting, otherwise it
    #is fetched as a string when decrypting, hence making it impossible to decrypt.
    
    with open(user_path, "a") as file:
        file.write(f"{encrypted_name.decode()} | {encrypted_username.decode()}, {encrypted_password.decode()}\n")
        print(f"Data has been saved for {platform_name}")
    
    
def view(fernet, username):
    user_path = f"files/{username}_data.txt"
    with open(user_path, "r") as file:
        for line in file:
            data = line
            for i in range(0, len(data)):
                if data[i] == "|":
                    platform = data[:i-1]
                    account = data[i+1:]
                    username, password = account.split(",")
                    
                    platform_decrypted = fernet.decrypt(platform.encode())
                    username_decrypted = fernet.decrypt(username.encode())
                    password_decrypted = fernet.decrypt(password.encode())
                    
                    print(f"Platform: {platform_decrypted.decode()}")
                    print(f"Username: {username_decrypted.decode()}")
                    print(f"Password: {password_decrypted.decode()}")

def update(username, fernet):
    user_path = f"files/{username}_data.txt"
    
    
def delete(username, fernet):
    ...

if __name__ == "__main__":
    main()