import os

print("Hello! \nWelcome to Te+!" + "\nInput your command:\n ")

while True:
    # Message cycle
    def cy():
        print("Message: ")
        cy1 = input()
        while(True):
            print(cy1)
    # Arithmetic operations
    def ep():
        print("Number 1: ")
        co = int(input())
        print("Number 2: ")
        co2 = int(input())
        print("Char: ")
        co1 = input()
        try:
            if co1 == "+":
                print("Result: " + str(co + co2))
            if co1 == "-":
                print("Result: " + str(co - co2))
            if co1 == "\*":
                print("Result: " + str(co * co2))
            if co1 == "/":
                print("Result: " + str(co / co2))
            if co1 == "%":
                print("Result: " + str(co % co2))
        except(ZeroDivisionError):
            print("Divide by zero!\n")
    # Obtaining path
    def gec():
        print(os.getcwd())
    # File sheet
    def L():
        os.listdir()
    # Creating a folder
    def fol():
        cf = input("Name folder: ")
        os.mkdir(cf)
    # File deletion
    def rfile():
        cr = input("Name: ")
        os.remove(cr)
    # Creating a file
    def fl():
        s = input("Name: ")
        f = open(s, "w")
        j = input("Want to enter text or you want to add? (YES, NO, ADD)\n")
        if j == "YES":
            t = input("Text: ")
            f.write(t)
            f.close()
        if j == "NO":
            f.close()
    # Read file
    def refol():
        t = input("Name: ")
        f = open(t, "r")
        print(f.read())
        f.close
    # Adding text to a file
    def afol():
        j = input("Name: ")
        f = open(j, "a")
        t = input("Text: ")
        f.write(t)
        f.close
    # Deleting a folder
    def rfol():
        n = input("Name: ")
        os.rmdir(n)
    # Changing the directory
    def chdr():
        t = input("Name: ")
        os.chdir(t)
    # File statistics
    def stat():
        t = input("Name file: ")
        print(os.stat(t))
    # Return to the previous directory
    def mcdr():
        os.chdir("..")
    # Renaming a file
    def reN():
        t = input("Name file: ")
        t1 = input("New name: ")
        os.rename(t, t1)
    # Creating subfolders
    def dr():
        t = input("Name folders: ")
        os.makedirs(t)
    # Changing the file path
    def rep():
        f = input("Name file: ")
        f1 = input("Path: ")
        os.replace(f, f1)
    # Name of the os
    def nm():
        print(os.name)
    # Variable dictionary
    def env():
        print(os.environ)
    # File/directory serch
    def sech():
        n = input("Name: ")
        print(os.getenv(n))
    # Is there a file
    def pse():
        n = input("Name: ")
        print(os.path.exists(n))
    # Current process id
    def idi():
        print(os.getpid())
    # File size
    def ges():
        N = input("Name: ")
        print(os.path.getsize(N))

    commmand = input()

    if commmand == "cy":
        cy()
    if commmand == "ep":
        ep()
    if commmand == "gec":
        gec()
    if commmand == "L+":
        L()
    if commmand == "<+":
        fol()
    if commmand == "<-=":
        rfile()
    if commmand == "<+=":
        fl()
    if commmand == "<-":
        rfol()
    if commmand == "<+=?":
        refol()
    if commmand == "<+=_":
        afol()
    if commmand == "<=>":
        chdr()
    if commmand == "St":
        stat()
    if commmand == "<_>":
        mcdr()
    if commmand == "reN":
        reN()
    if commmand == "<dr":
        dr()
    if commmand == "rep":
        rep()
    if commmand == "nm":
        nm()
    if commmand == "env":
        env()
    if commmand == "sech":
        sech()
    if commmand == "p?":
        pse()
    if commmand == "id":
        idi()
    if commmand == "ges":
        ges()


