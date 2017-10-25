#Chat Application Regisration
import sys
print "Do you want to Sign Up or Sign In?"
print "Press U for Sign Up!"
print "Press I for Sign In!"
ch = input("Enter your Response: ")
print (ch)
if (ch == 'U'):
    f = open('my.txt', 'a+')
    name = input ("Enter your desired username = ")
    name = name.encode()
    position = 0
    str = f.read()
    if name in str:
        print "Username is taken"
        print "Please choose another username"
        exit()
    else:
        print "Username not Found"
        f.write(name)
    age = input("Enter your age = ")
    if(age < '13' or age > '60'):
        print"You are not allowed"
        exit()
    else:
        print"You are allowed"
    f.write(age)
    f.close()
    f1 = open('my1.txt' , 'a+')
    password = input("Make your password(6 Characters only) = ")
    l = len(password)
    if(l > '6'):
        print "Password should be 6 Characters"
        exit()
    else:
        print "Password is 6 Characters"
        print "Your Username and password is saved"
        f1.write(password)
    f1.close()
elif (ch == 'I'):
    f = open('my.txt', 'a+')
    name1 = input("Enter your username = ")
    name1 = name1.encode()
    position = 0
    str = f.read()
    if name1 in str:
        print('Found')
    else:
        print("Wrong Username!!")
        exit()
    f.close()
    f1 = open('my1.txt', 'a+')
    password1 = input("Enter your password = ")
    password1 = password1.encode()
    position = 0
    str = f1.read()
    if password1 in str:
        print('Found')
        print("Correct!")
    else:
        print("Wrong Password!!")
        exit()
    f1.close()



