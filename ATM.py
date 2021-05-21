import random
import time
print("")
print("Welcome to this ATM!!")
print("Here, you're provided with 1000$ and a earner which can be upgraded by your balance.")
print("There are several modes for this ATM.")
print("Press S to see all your balances.")
print("Press U to upgrade your earner level.")
print("Press H to hack")
print("Press W to withdraw your hacked balance")
print("Press E to exit")
print("")

startTime= time.time()

class ATM (object):
    def __init__(self, balance, hackedMoney, earnerLevel, offlineEarnings):
        self.balance = balance
        self.hackedMoney = hackedMoney
        self.earnerLevel = earnerLevel
        self.offlineEarnings = offlineEarnings

    def inputMode(self):
        while(True):
            print("")
            mode = input("Enter the mode you want = ")
            if(mode == "S" or mode == "s"):
                print("Your Balance : " + str(self.balance))
                print("Hacked money : " + str(self.hackedMoney))
                print("Earner Level : " + str(self.earnerLevel) + ', Offline Earnings : + $'+ str(self.offlineEarnings) + '/10 sec')
            elif(mode == "H" or mode == "h"):
                hacking(self)
            elif(mode == "W" or mode == "w"):
                withdraw(self)
            elif(mode == "E" or mode == "e"):
                exit()
            elif(mode == "U" or mode == "u"):
                upgradeEarner(self)
            else:
                print("Wrong Mode!!")

def hacking(self):
    print(self.hackedMoney)
    print("")
    print("Entered Hacked Mode")
    randomNumber = random.randint(10000, 99999)
    print("Your number : " + str(randomNumber))
    inputedNumber = int(input("Enter the number : "))
    if(inputedNumber == randomNumber and self.hackedMoney == 0):
        changeHackedMoney(self, 250, 'l')
    elif(inputedNumber == randomNumber and self.hackedMoney != 0):
        changeHackedMoney(self, self.hackedMoney + self.hackedMoney, 'l')
    else:
        print("Wrong Number")
        atm.inputMode()

def withdraw(self):
    self.balance = self.balance + self.hackedMoney
    changeHackedMoney(self, 0, 'm')
    print("Withdrawn Successfully")

def changeHackedMoney(self, hackedMoney, m):
    self.hackedMoney = hackedMoney
    if(m != 'm'):
        print('+' + str(self.hackedMoney) + '$')

def upgradeEarner(self):
    self.earnerLevel = self.earnerLevel + 1
    if(self.earnerLevel == 1 and self.balance != 0):
        addOfflineEarnings(self, 100)
        self.balance = self.balance-100
    elif(self.earnerLevel == 2 and self.balance != 0):
        addOfflineEarnings(self, 200)
        self.balance = self.balance-200
    elif(self.earnerLevel == 3 and self.balance != 0):
        addOfflineEarnings(self, 500)
        self.balance = self.balance-500
    elif(self.earnerLevel > 3 and self.balance != 0):
        addOfflineEarnings(self, self.offlineEarnings + self.offlineEarnings)
        self.balance = self.balance-(self.offlineEarnings + self.offlineEarnings)
    if(self.balance == 0):
        print("You are not having enough money :(")

def addOfflineEarnings(self, increaseBy):
    if(time.time() - startTime >= 5):
        self.offlineEarnings = self.offlineEarnings + increaseBy

atm = ATM(1000, 0, 0, 0)
atm.inputMode()
addOfflineEarnings()