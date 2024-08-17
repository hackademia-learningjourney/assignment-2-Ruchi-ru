print('1.Sign up \n 2.Sign in')

choice = int(input("Enter your choice: "))

if choice == 1:

    username = input("Enter your username: ")

    password = input("Enter your password: ")

    mob_number = input("Enter your mobile number: ")

    with open('signupinfo.txt', 'a') as f:

        f.write( username + ' ' + password + ' ' + mob_number + '\n')

else:

    flag= 0

    username = input("Enter your username: ")

    password = input("Enter your password: ")

    with open('signupinfo.txt', 'r') as f:

        for x in f.readlines():

            values = x.split(' ')

            if(username == values[0] and password == values[1]):

                print("welcome to the program")

                print("your information")

                print("username: " + values[0])

                print("password: " + values[1])

                print("mobile: " + values[2])

                flag = 0

                break

            else:

                flag = 1

    if(flag == 1):

        print("Login Error")