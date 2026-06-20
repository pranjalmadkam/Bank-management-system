# banking management system

import user

# user.create()
Ask=input("waht you want to do:\n" 
"1.create account\n" 
"2.login \n"
"Enter your choice:")
if(Ask=="1"):
  user.create()
elif(Ask=="2"):  
 name=input("Enter your name:")
 user.display(name)
else:
  print("Invalid Choice") 