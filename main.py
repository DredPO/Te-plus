import os
from rich.progress import Progress
from rich.console import Console
import time
from rich.panel import Panel

with Progress() as prog:
    task = prog.add_task("[green]Loading...", total=100)

    while not prog.finished:
        prog.update(task, advance=1)
        time.sleep(0.02)

cons = Console(width=21)
cons.print(Panel.fit("[bold green]TE+\n[/bold green][bold blue]Version: 2.0[/bold blue]"))
cons.print("---------------------")
cons.print("[uu yellow]\n\aInput your command:\n [/uu yellow]")

while True:
    # Message cycle
    def cy():
        print("Message: ")
        cy1 = input()
        while True:
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
            if co1 == "/*":
                print("Result: " + str(co * co2))
            if co1 == "/":
                print("Result: " + str(co / co2))
            if co1 == "%":
                print("Result: " + str(co % co2))
        except ZeroDivisionError:
            print("Divide by zero!\n")


    # Obtaining path
    def gec():
        cons.print(Panel.fit(os.getcwd()))


    # File sheet
    def L():
        cons.print(str(os.listdir()))


    # Creating a folder
    def fol():
        cf = input("Name folder: ")
        os.mkdir(cf)
        print("Ready!")

    # File deletion
    def rfile():
        cr = input("Name: ")
        os.remove(cr)
        print("Ready!")


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
        f.close()


    # Adding text to a file
    def afol():
        j = input("Name: ")
        f = open(j, "a")
        t = input("Text: ")
        f.write(t)
        f.close()
        print("Ready!")

    # Deleting a folder
    def rfol():
        n = input("Name: ")
        os.rmdir(n)
        print("Ready")


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
        cons.print(Panel.fit(os.name))


    # Variable dictionary
    def env():
        cons.print(Panel.fit(str(os.environ)))


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
        cons.print(Panel.fit(str(os.getpid())))


    # File size
    def ges():
        N = input("Name: ")
        print(str(os.path.getsize(N)))

    # Cleaning window
    def cle():
        os.system('cls||clear')


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
    if command == "cle":
        cle()

