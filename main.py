from User import *
from os import system
import time
print("hi")

run = True
while run:
    system("cls")
    system("color 03")
    try:
        choice = int(input("1>Sign in\n2>Log in\n0>EXIT\n>>>"))
        if choice in (1, 2):
            if choice == 1:
                user = User()
                if user.signIn():
                    singedIn = True
                else:
                    system("color 04")
                    print("Invalid  userName")
                    time.sleep(2)
                    continue
                while singedIn:
                    try:
                        system("cls")
                        system("color 02")
                        print("WELCOME ", user.data['userName'])
                        toDo = int(input("1> Enter link of new product to track\n2> Track Previous products\n0> Sign Out\n>>>"))
                        if toDo in (1,2):
                            if toDo == 1:
                                system("cls")
                                system("color 04")
                                link = input("Please at this point I don have any link cheker in Action so \nENTER A VALID LINK >>>")
                                user.fetchData(link)
                                # user.productList()
                            elif toDo == 2:
                                system("cls")
                                print("PRODUCT NAME                      ||   PRICE\n-------------------------------------------------")
                                print(user.productList())

                        elif toDo == 0:
                            print("Signed Out!!!")
                            singedIn = False
                    except ValueError:
                        system("color 04")
                        print("Invalid Input!!!")
                        time.sleep(1)

            elif choice == 2:
                user = User()
                user.login()
                system("cls")
                print("\nProfile Created\n Sign IN now with same credentials !!!")
                continue

        elif choice == 0:
            print("BYE!!!")
            exit()
    except ValueError:
        system("color 04")
        print("Invalid Input!!!")
        time.sleep(1)

    else:
        print("Invalid input")
