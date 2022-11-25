import os

print("Hello! \nWelcome to Te+!" + "\nInput your command:\n ")

while True:
    def cy():
        print("Message: ")
        cy1 = input()
        while(True):
            print(cy1)
    def ep():
        print("Divide by zero!\n")
        print("Number 1: ")
        co = int(input())
        print("Number 2: ")
        co2 = int(input())
        print("Char: ")
        co1 = input()
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
    def gec():
        print(os.getcwd())
    def L():
        os.listdir()
    def fol():
        cf = input("Name folder: ")
        os.mkdir(cf)
    def rfile():
        cr = input("Name: ")
        os.remove(cr)
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
    def refol():
        t = input("Name: ")
        f = open(t, "r")
        print(f.read())
        f.close
    def afol():
        j = input("Name: ")
        f = open(j, "a")
        t = input("Text: ")
        f.write(t)
        f.close
    def rfol():
        n = input("Name: ")
        os.rmdir(n)
    def chdr():
        t = input("Name: ")
        os.chdir(t)
    def stat():
        t = input("Name file: ")
        print(os.stat(t))
    def mcdr():
        os.chdir("..")
    def reN():
        t = input("Name file: ")
        t1 = input("New name: ")
        os.rename(t, t1)
    def dr():
        t = input("Name folders: ")
        os.makedirs(t)
    def rep():
        f = input("Name file: ")
        f1 = input("Path: ")
        os.replace(f, f1)
    def nm():
        print(os.name)
    def env():
        print(os.environ)
    def sech():
        n = input("Name: ")
        print(os.getenv(n))
    def pse():
        n = input("Name: ")
        print(os.path.exists(n))
    def idi():
        print(os.getpid())
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


