
def register():
    username = str(input("Username: "))
    password = input("Password: ")
    add(username, password)


def login():
    username = str(input("Username: "))
    password = input("Password: ")
    validate(username, password)
    

def add(username, password):
    filehandler = open("stored-data.txt", "r+")
    if username in filehandler.read():
        print("Username already in use")
        register()
    else:
        filehandler.write("\n" + username + " " + password + "\n")
        filehandler.close()
        print("Log in")
        login()

def validate(username, password):
    filehandler = open("stored-data.txt", "r")
    filecontent = filehandler.read()
    infolist = filecontent.split()
    try: 
        userindex = infolist.index(username)
        passwordindex = userindex + 1
        if username in infolist and password == infolist[passwordindex]:
            print("You're in")
            filehandler.close()
    except:
        filehandler.close()
        print("Your password or your username is not correct" + "\n" + "1)Try again" + "\n" + "2) Register")
        option = int(input("Select the option number: "))
        if option == 1:
            login()
        elif option == 2:
            register()
        else:
            print("Select a valid number")
        
   


def homepage():
    print("Welcome!\n1) Log in\n2) Register")
    option = int(input("Select the option number: "))
    if option == 1:
        login()
    elif option == 2:
        register()
    else:
        print("Select a valid number")
        homepage()

homepage()


    

