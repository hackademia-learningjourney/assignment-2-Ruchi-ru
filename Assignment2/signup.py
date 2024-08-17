import json
import os

file_path = "users_data.json"

def load_user_data():
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            return json.load(file)
    return {}

def save_user_data(data):
    with open(file_path, 'w') as file:
        json.dump(data, file)

def sign_up():
    username = input("Username: ")
    password = input("Password: ")
    mobile = input("Mobile number: ")

    users = load_user_data()
    users[username] = {"password": password, "mobile": mobile}
    save_user_data(users)
    print("Sign up successful!")

def sign_in():
    username = input("Username: ")
    password = input("Password: ")

    users = load_user_data()
    if users.get(username) and users[username]["password"] == password:
        print(f"Welcome! Your mobile number is {users[username]['mobile']}")
    else:
        print("Incorrect credentials.")

def main():
    choice = input("1. Sign Up\n2. Sign In\nChoose (1/2): ")
    if choice == "1":
        sign_up()
    elif choice == "2":
        sign_in()
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
