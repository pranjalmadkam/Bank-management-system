# all calculation work

def calc(username):
    with open("users.txt", "r") as user:
        content = user.readlines()

    process = input("1.Deposit\n2.Withdrawl\nEnter: ")

    # amount = int(input("Enter amount: "))

    with open("users.txt", "w") as user:
        for line in content:
            name, age, password, balance = line.strip().split(",")

            if name == username:
                balance = int(balance)

                if process == "1":
                    amount = int(input("Enter amount: "))
                    balance += amount
                    print("Deposited Successfully")

                elif process == "2":
                    amount = int(input("Enter amount: "))
                    if amount > balance:
                        print("Insufficient balance")
                    else:
                        balance -= amount
                        print("Withdrawn Successfully")
        
                else:
                    print("Invalid Choice")        

                line = f"{name},{age},{password},{balance}\n"    

                
            user.write(line)