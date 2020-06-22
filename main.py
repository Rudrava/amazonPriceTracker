from User import *
print("hi")

run = True
while run:
    choice = int(input("1>Sign in\
                        2>Log in\
                        0>EXIT\n>>>"))
    if choice in (1, 2):
        if choice == 1:
            user = User()
            if user.signIn():
                singedIn = True
            else:
                print("Invalid  userName")
                continue
            print("WELCOME ", user.data['userName'])
            while singedIn:
                toDo = int(input("1> Enter link of new product to track\
                                  2> Track Previous products\
                                  0> Exit\n>>>"))
                if toDo in (1,2):
                    if toDo == 1:
                        link = input("Please at this point I don have any link cheker in Action so \
                                    ENTER A VALID LINK >>>")
                        link = '"' + link + '"'
                        print(link)
                        user.fetchData(link)
                        user.productList()
                    elif toDo == 2:
                        print(user.productList())

                elif toDo == 0:
                    print("Signed Out!!!")
                    singedIn = False
        elif choice == 2:
            user = User()
            user.login()
            print("Profile Created\n Sign IN now with same credentials !!!")
            continue

    elif choice == 0:
        print("BYE!!!")
        exit()

    else:
        print("Invalid input")
