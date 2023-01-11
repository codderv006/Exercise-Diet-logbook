'''
Instructions:
Create a food log file for each client
Create an exercise log file for each client.
Ask the user whether they want to log or retrieve client data.
Write a function that takes the user input of the client's name. After the client's name is entered, it will display a message as "What you want to log- Diet or Exercise".
Use function
def getdate():
           import datetime
           return datetime.datetime.now()
The purpose of this function is to give time with every record of food or exercise added in the file.
Write a function to retrieve exercise or food file records for any client.
You are advised to participate in solving this problem. This task helps you to become a good problem solver and enables you to accept the challenge and acquire new skills.

'''

def getdate():
    import datetime
    return datetime.datetime.now()
print("Welcome to health management system here you can log you Exercise and Diet data")
x=input("Enter your Name: ")


if x=="Vedant":
    y=input("Enter which logbook you want to access\n 1. For Diet log\t 2. For Exercise log: \n")
    if y=="1":
        while (y=="1"):
            j= input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j=="1":
                f = open("Vedant_d.txt", "r")
                for line in f:
                    print(line, end="")
            elif j=="2":
                f = open("Vedant_d.txt", "a")
                k=input("Enter what diet you took: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j=="E":
                break


    else:
        while (y == "2"):
            j= input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j == "1":
                f = open("Vedant_e.txt", "r")
                for line in f:
                    print(line, end="")
            elif j=="2":
                f = open("Vedant_e.txt", "a")
                k = input("Enter which exercise you did: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j == "E":
                break

elif x == "Nayan":
    y = input("Enter which logbook you want to access\n 1. For Diet log\t 2. For Exercise log: \n")
    if y == "1":
        while (y == "1"):
            j = input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j == "1":
                f = open("Nayan_d.txt", "r")
                for line in f:
                    print(line, end="")
            elif j == "2":
                f = open("Nayan_d.txt", "a")
                k = input("Enter what diet you took: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j == "E":
                break


    else:
        while (y == "2"):
            j = input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j == "1":
                f = open("Nayan_e.txt", "r")
                for line in f:
                    print(line, end="")
            elif j == "2":
                f = open("Nayan_e.txt", "a")
                k = input("Enter which exercise you did: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j == "E":
                break

elif x == "Trel":
    y = input("Enter which logbook you want to access\n 1. For Diet log\t 2. For Exercise log: \n")
    if y == "1":
        while (y == "1"):
            j = input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j == "1":
                f = open("Trel_d.txt", "r")
                for line in f:
                    print(line, end="")
            elif j == "2":
                f = open("Trel_d.txt", "a")
                k = input("Enter what diet you took: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j == "E":
                break


    else:
        while (y == "2"):
            j = input("\nPress 1. To read existing data\t 2. To add new data and E to exit: \n")
            if j == "1":
                f = open("Trel_e.txt", "r")
                for line in f:
                    print(line, end="")
            elif j == "2":
                f = open("Trel_e.txt", "a")
                k = input("Enter which exercise you did: \n")
                f.write(f'\n{k}  ')
                f.write(str(getdate()))
            elif j == "E":
                break

else:
    print("Invalid input.")
