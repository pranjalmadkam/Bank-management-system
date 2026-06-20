# user login and logout

import hashlib
import login

def create():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    password = input("Enter your password: ")
    with open("pass.txt", "a") as user:
        user.write(f"{name},{password}\n")

    balance = int(input("Enter initial balance: "))

    hashed_pass = hashlib.sha256(password.encode()).hexdigest()

   
    with open("users.txt", "a") as user:
        user.write(f"{name},{age},{hashed_pass},{balance}\n")

    print("ACCOUNT SUCCESSFULLY CREATED")


def display(username):
    import hashlib
    password = input("enter your password:")
    hashed_input = hashlib.sha256(password.encode()).hexdigest()

    found = False

    with open("pass.txt","r") as user:
        for line in user:
            name,stored_pass,= line.strip().split(",")

            if name == username:
                found = True
                print("LOGIN SUCCESSFULLY")
                if password== stored_pass:
                    with open("users.txt", "r") as user:
                      content = user.readlines()
                      print("<==== LOADING YOUR DATA ====>")
        
                      for line in content:
                        name, age, password, balance = line.strip().split(",")
                        if name==username:
                          print(f"\n--- USER DETAILS ---")
                          print(f"Name     : {username}")
                          print(f"Age      : {age}")
                          print(f"Balance  : ₹{balance}")   
                    transaction=input("You want to do any Transaction (Yes/NO):")
                    if (transaction=="Yes" or transaction=="yes"):                                
                     login.calc(username) 
                    else:
                       break
                else:
                    print("INCORRECT PASSWORD")
                break

    if not found:
        print("USER NOT FOUND")