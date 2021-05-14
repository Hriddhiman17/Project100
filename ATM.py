import random

balance = 1000
hackedMoney = 0
print("")
print("Welcome to this ATM!!")
print("Here, you're provided with 1000$.")
print("There are several modes for this ATM.")
print("Press S to see all your balances.")
print("Press H to hack")
print("Press W to withdraw your hacked balance")
print("Press E to exit")
print("")
print("My Balance : " + str(balance))
print("Hacked money : " + str(hackedMoney))

def inputMode():
    print("")
    mode = input("Enter the mode you want = ")
    if(mode == "S" or mode == "s"):
        print("Your Balance : " + str(balance))
        print("Hacked money : " + str(hackedMoney))
        inputMode()
    elif(mode == "H" or mode == "h"):
        hacking()
    elif(mode == "W" or mode == "w"):
        withdraw()
    elif(mode == "E" or mode == "e"):
        exit()
    else:
        print("Wrong Mode!!")
        inputMode()


def hacking():
    print("")
    print("Entered Hacked Mode")
    randomNumber = random.randint(100, 999)
    print("Your number : " + str(randomNumber))
    inputedNumber = input("Enter the number : ")
    print(inputedNumber)
    if(randomNumber == inputedNumber):
        hackedMoney = hackedMoney+250
        print(hackedMoney)
    elif(inputedNumber == randomNumber and hackedMoney != 0):
        hackedMoney = hackedMoney*hackedMoney
        print(hackedMoney)
    else:
        print("Wrong Number")
    inputMode()


def withdraw():
    balance = balance + hackedMoney
    hackedMoney = 0
    print("Withdrawn Successfully")


class ATM (object):
    def __init__(self, myBalance):
        self.myBalance = myBalance


inputMode()
