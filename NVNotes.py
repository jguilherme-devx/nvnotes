import time
import subprocess as sp
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path

try:
    sp.run(["mkdir", "/data/data/com.termux/files/home/.config/NVNotes"])
except:
    pass

console = Console()
saves = "/data/data/com.termux/files/home/.config/NVNotes"
pasta = Path("/data/data/com.termux/files/home/.config/NVNotes")
title = "/data/data/com.termux/files/home/NVNotes-project/title.txt"
notes_totais = []

for notes in pasta.iterdir():
    notes_totais.append(notes.name)

def clear():
    sp.run(["clear"])

clear()
print("Welcome to NVNotes")
time.sleep(0.5)


def remove():

    print("\nnotes:")
    sp.run(["ls", saves])
    nome = input("type the name of the note: ")
    try:
        with open(f"{saves}/{nome}") as n:
            escolha = input(f"remove {nome} [yes or no]?\n~>")
        if escolha == "yes":
            print("apagando...")
            time.sleep(0.5)
            sp.run(["rm", f"{saves}/{nome}"])
            time.sleep(0.5)
            clear()
        else:
            pass
    except:
        print("non-existent note")

def edit():

    print("\nnotes:")
    sp.run(["ls", saves])
    nome = input("type the name of the note: ")
    if nome in notes_totais:
        sp.run(["nvim", f"{saves}/{nome}"])
        clear()
    else:
        print("non-existent note")

def view():

    while True:
        print("\nnotes:")
        sp.run(["ls", saves])
        nome = input("type the name of the note: ")

        try:
            if not nome.endswith(".md"):
                with open(f"{saves}/{nome}") as note:
                    sp.run(["cat", f"{saves}/{nome}"])

            else:

                with open(f"{saves}/{nome}") as note:
                    md = Markdown(note.read())
                clear()
                console.print(md)

            print("\n \n")
            input("Press Enter to continue...")
            break

        except:
            print("non-existent note")

def create():
    nome = input("\ntype the name of the note: ")
    time.sleep(0.5)

    if nome in notes_totais:
        print("existent note")
    else:
        sp.run(["nvim", f"{saves}/{nome}"])
        clear()

def menu():

    sp.run(["cat", title])
    print("[1] create new note")
    print("[2] view note")
    print("[3] edit note")
    print("[4] Remove note")
    print("[5] exit")

    escolha = input("~>> ")

    time.sleep(0.5)
    if escolha == "1":
        create()
    elif escolha == "2":
        view()
    elif escolha == "3":
        edit()
    elif escolha == "4":
        remove()
    elif escolha == "5":
        clear()
        return True;
    else:
        print("\033[1;31m[!command invalid!]\033[0m")

while True:
    resultado = menu()
    if resultado:
        break

