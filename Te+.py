import os
from colorama import Fore

print(Fore.BLUE + "\t\t\t\t\t\t\t\t\t\t\t\tTE+\n\t\t\t\t\t\t\t\t\t\t\tVersion: 2.0")
print(Fore.BLUE + "\t\t\t\t\t\t\t\t\t\t--------------------")
print(Fore.LIGHTGREEN_EX + "\n\aInput your command:\n ")

while True:
    # Message cycle
    def cy():
        print(Fore.LIGHTGREEN_EX + "Message: ")
        cy1 = input()
        while True:
            print(cy1)


    # Arithmetic operations
    def ep():
        print(Fore.LIGHTGREEN_EX + "Number 1: ")
        co = int(input())
        print(Fore.LIGHTGREEN_EX + "Number 2: ")
        co2 = int(input())
        print(Fore.LIGHTGREEN_EX + "Char: ")
        co1 = input()
        try:
            if co1 == "+":
                print(Fore.LIGHTGREEN_EX + "Result: " + str(co + co2))
            if co1 == "-":
                print(Fore.LIGHTGREEN_EX + "Result: " + str(co - co2))
            if co1 == "/*":
                print(Fore.LIGHTGREEN_EX + "Result: " + str(co * co2))
            if co1 == "/":
                print(Fore.LIGHTGREEN_EX + "Result: " + str(co / co2))
            if co1 == "%":
                print(Fore.LIGHTGREEN_EX + "Result: " + str(co % co2))
        except ZeroDivisionError:
            print(Fore.LIGHTRED_EX + "Divide by zero!\n")


    # Obtaining path
    def gec():
        print(Fore.LIGHTGREEN_EX + os.getcwd())


    # File sheet
    def L():
        return Fore.LIGHTGREEN_EX + str(os.listdir())


    # Creating a folder
    def fol():
        cf = input(Fore.LIGHTGREEN_EX + "Name folder: ")
        os.mkdir(cf)
        print(Fore.LIGHTGREEN_EX + "Ready!")

    # File deletion
    def rfile():
        cr = input(Fore.LIGHTGREEN_EX + "Name: ")
        os.remove(cr)
        print(Fore.LIGHTGREEN_EX + "Ready!")


    # Creating a file
    def fl():
        s = input(Fore.LIGHTGREEN_EX + "Name: ")
        f = open(s, "w")
        j = input(Fore.LIGHTGREEN_EX + "Want to enter text or you want to add? (YES, NO, ADD)\n")
        if j == "YES":
            t = input(Fore.LIGHTGREEN_EX + "Text: ")
            f.write(t)
            f.close()
        if j == "NO":
            f.close()


    # Read file
    def refol():
        t = input(Fore.LIGHTGREEN_EX + "Name: ")
        f = open(t, "r")
        print(f.read())
        f.close()


    # Adding text to a file
    def afol():
        j = input(Fore.LIGHTGREEN_EX + "Name: ")
        f = open(j, "a")
        t = input("Text: ")
        f.write(t)
        f.close()
        print(Fore.LIGHTGREEN_EX + "Ready!")

    # Deleting a folder
    def rfol():
        n = input(Fore.LIGHTRED_EX + "Name: ")
        os.rmdir(n)
        print(Fore.LIGHTGREEN_EX + "Ready")


    # Changing the directory
    def chdr():
        t = input(Fore.LIGHTGREEN_EX + "Name: ")
        os.chdir(t)


    # File statistics
    def stat():
        t = input(Fore.LIGHTGREEN_EX + "Name file: ")
        print(os.stat(t))


    # Return to the previous directory
    def mcdr():
        os.chdir("..")


    # Renaming a file
    def reN():
        t = input(Fore.LIGHTGREEN_EX + "Name file: ")
        t1 = input(Fore.LIGHTGREEN_EX + "New name: ")
        os.rename(t, t1)


    # Creating subfolders
    def dr():
        t = input(Fore.LIGHTGREEN_EX + "Name folders: ")
        os.makedirs(t)


    # Changing the file path
    def rep():
        f = input(Fore.LIGHTGREEN_EX + "Name file: ")
        f1 = input(Fore.LIGHTGREEN_EX + "Path: ")
        os.replace(f, f1)


    # Name of the os
    def nm():
        print(Fore.LIGHTBLUE_EX + os.name)


    # Variable dictionary
    def env():
        print(Fore.LIGHTBLUE_EX + str(os.environ))


    # File/directory serch
    def sech():
        n = input(Fore.LIGHTGREEN_EX + "Name: ")
        print(Fore.LIGHTGREEN_EX + os.getenv(n))


    # Is there a file
    def pse():
        n = input(Fore.LIGHTGREEN_EX + "Name: ")
        print(os.path.exists(n))


    # Current process id
    def idi():
        print(Fore.LIGHTYELLOW_EX + str(os.getpid()))


    # File size
    def ges():
        N = input(Fore.LIGHTGREEN_EX + "Name: ")
        print(Fore.LIGHTGREEN_EX + str(os.path.getsize(N)))


    command = input()

    if command == "cy":
        cy()
    if command == "ep":
        ep()
    if command == "gec":
        gec()
    if command == "L+":
        L()
    if command == "<+":
        fol()
    if command == "<-=":
        rfile()
    if command == "<+=":
        fl()
    if command == "<-":
        rfol()
    if command == "<+=?":
        refol()
    if command == "<+=_":
        afol()
    if command == "<=>":
        chdr()
    if command == "St":
        stat()
    if command == "<_>":
        mcdr()
    if command == "reN":
        reN()
    if command == "<dr":
        dr()
    if command == "rep":
        rep()
    if command == "nm":
        nm()
    if command == "env":
        env()
    if command == "sech":
        sech()
    if command == "p?":
        pse()
    if command == "id":
        idi()
    if command == "ges":
        ges()
