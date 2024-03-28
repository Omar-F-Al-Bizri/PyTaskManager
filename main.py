from classes import *

manager = TaskManager()

def main():
    program_on = True

    while (program_on):
        manager.displayQueue()
        manager.peekDisplay()

        action = input("What to do?\n")

        if (action == "quit"):
            program_on = False
    
    print("Quitting Program")

main()