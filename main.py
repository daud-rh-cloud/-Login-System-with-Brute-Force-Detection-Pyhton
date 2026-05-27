
users= {}
content = ''
user_input = ''
Password_cheaks= ''
attemmts = {}  

while user_input != "4": 
    print ("=== Login System === ")
    print ("1. Register ")
    print ("2. Login ")
    print ("3. Show all users ")
    print("4. Exit")
    user_input= input("Choose a Nummer: ")

    if user_input == "1" :
        Username= input ("Enter a UserName: ")
        Password= input ("Enter a password: ")
        
        #Password Cheak----
        if Username in users :
            print ("The UserName Already Exist")
 
        else:
          while len(Password) < 8 or  Password.islower() == True: 
           print ("WeakPaasword! Minimum 8 character & one uppercase") 
           Password= input ("Enter a password: ")
        
        print ("User Succecfully Created! ")
        users [Username]= Password
        attemmts[Username] = 0 ### Assining a early value to track password attempt later!

    elif user_input == "2": 
        username_login = input("Enter the username: ")
        if username_login not in users :
         print ("UserName is not found!! ") 

        elif attemmts[username_login] >= 6 : 
          print ("Account is Locked! ")

        else: 
         login = ''
         while login != "Succecfull" and attemmts[username_login] < 6 : 
          Password_login = input("Enter the PASSWORD: ")
  
          if users [username_login] != Password_login:
            print("wrong Passsword !!")
            attemmts[username_login] += 1
          else: 
           print("Login Sucessfull !!")
           login = "Succecfull"




    elif user_input == "3":
        for x , y in users.items(): 
          print ("-------------")
          print ("Name: ", x)
          print ("Password: ",y)
          print ("=====================") 

    elif user_input == "4": 
      print ("------GoodBYE--------")
      break 


            
          
