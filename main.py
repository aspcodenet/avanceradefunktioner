#1.  Multiple Returns
#       Use case: Minska antalet loopar - dvs 
#                 Returnera kalkylerat värde + FELKOD/FELSTRÄNG

from dataclasses import dataclass
import barnum
from datetime import date
import random
import time
from timeit import default_timer

def timing_decorator(funktionsAliaset):
    def wrapper(*args, **kwargs):
        start = default_timer()
        x = funktionsAliaset(*args, **kwargs)
        end = default_timer()
        print(f"Det tog {end-start}")
        return x 
    return wrapper


def print_decorator(funktionsAliaset):
    def wrapper(*args, **kwargs):
        print("Starting")
        x = funktionsAliaset(*args, **kwargs)
        print("Ending")
        return x 
    return wrapper

@print_decorator
@timing_decorator
def CalculateSalaryIgen(): # SRP = endast detta
    # på riktigt en beräkning
    time.sleep(1)
    return 100

@timing_decorator
def CalculateSalarySpecial(age, namn): # SRP = endast detta
    # på riktigt en beräkning
    time.sleep(2)
    return 200



def mainDecorator():
    x = CalculateSalaryIgen()
    x2 = CalculateSalarySpecial(12, "332134242")
    print(x)


def generate_power(exponent):
    def power(base):
        return base ** exponent
    return power    

raise_by_two = generate_power(2)   # x upphöjt 2
raise_by_three = generate_power(3)# x upphöjt 3

def mainFuncGen():
    x = raise_by_two(10) # 10 upph 2
    x = raise_by_three(10) # 10 upph 3
    r =  100
    return r


def CalculateBlabla(age, namn): # SRP 
    r =  200
    return r    
# def CalculateWhatever(): 
#     print("Starting")
#     x =  200 
#     print("Ending")
#     return x
def print_decorator(funktionsAliaset):
    print("Starting")
    x = funktionsAliaset()
    print("Ending")
    return x

def mainFunc():
    # funktionsAlias = CalculateSalary
    # res = print_decorator(funktionsAlias)
    res = print_decorator(CalculateSalary)





    alias = CalculateSalary
    print(alias)
    res = alias()

    d = CalculateSalary()


def calculateTotalSum(*args):
    totalSum = 0
    for num in args:
        totalSum += num
    return totalSum


def printTotalSum( printBeforeText, printAfterText, *args):
    print(printBeforeText)
    totalSum = 0
    for num in args:
        totalSum += num
    print(totalSum)
    print(printAfterText)


def team_print( lagnamn, *args):
    print(lagnamn + " har vunnit ")
    for year in args:
        print(year)

def logToFile(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

    

def mainMultiParams():
    logToFile(error="Ngt gick fel", code=404)
    logToFile(info="Programmet startas nu", varde="ABC123")


    team_print("Luleå HF", "1996")
    team_print("Leksands IF", "1969", "1973", "1974", "1975")



    printTotalSum("Nu startar beräkningen", "Klart",12,444,566,2)
    printTotalSum("Nu startar beräkningen", "Klart",12)

    r = calculateTotalSum(12, 11)
    r = calculateTotalSum(12)
    r = calculateTotalSum(12, 11,324,324423432,243243)
    a = 99
    b = 111
    print(12)
    print("asdsadsadds",a, "333", b)


@dataclass
class Player:
    Namn: str
    BirthDate: date
    JerseyNumber: int

def GetOldest(allPlayers:list[Player]) -> (Player):
    oldestPlayer = allPlayers[0]
    for player in allPlayers:
        if player.BirthDate < oldestPlayer.BirthDate:
            oldestPlayer = player
    return oldestPlayer


def GetYoungest(allPlayers:list[Player]) -> (Player):
    youngestPlayer = allPlayers[0]
    for player in allPlayers:
        if player.BirthDate > youngestPlayer.BirthDate:
            youngestPlayer = player
    return youngestPlayer

# kom ihåg visa "failsafe"
def GetOldestAndYoungest(allPlayers:list[Player]) -> (Player, Player):
    youngestPlayer = allPlayers[0]
    oldestPlayer = allPlayers[0]
    for player in allPlayers:
        if player.BirthDate > youngestPlayer.BirthDate:
            youngestPlayer = player
        if player.BirthDate < oldestPlayer.BirthDate:
            oldestPlayer = player
    return oldestPlayer, youngestPlayer



@dataclass
class PlayerResult:
    Oldest: Player
    Youngest: Player

def GetOldestAndYoungest2(allPlayers:list[Player]) -> PlayerResult:
    youngestPlayer = allPlayers[0]
    oldestPlayer = allPlayers[0]
    for player in allPlayers:
        if player.BirthDate > youngestPlayer.BirthDate:
            youngestPlayer = player
        if player.BirthDate < oldestPlayer.BirthDate:
            oldestPlayer = player
    
    return PlayerResult( oldestPlayer, youngestPlayer)



def mainHockey():
    listan = []
    for x in range(100000):
        p = Player(barnum.create_name(True),barnum.create_birthday(), random.randint(1,100) )
        listan.append(p)
    #oldest, youngest = GetOldestAndYoungest(listan)
    result = GetOldestAndYoungest2(listan)
    print(result.Oldest.Namn)
    # oldest = GetOldest(listan)
    # youngest = GetYoungest(listan)
    print(oldest.Namn)
    print(youngest.Namn)

    

def getlargest(numbers:list[int]) -> int:
    largest = numbers[0]
    for x in numbers:
        if x > largest:
            largest = x
    return largest

def getsmallest(numbers:list[int]) -> int:
    smallest = numbers[0]
    for x in numbers:
        if x <  smallest:
            smallest = x
    return smallest

def getLargestAndSmallest(numbers:list[int])  -> (int,int, str):
    if len(numbers) == 0:
        return None,None, "Listan är ju tom!!!"
    smallest = numbers[0]
    largest = numbers[0]
    for x in numbers:
        if x <  smallest:
            smallest = x
        if x > largest:
            largest = x
    return smallest, largest, ""

        

def main():
    listan = [12,11,456,12]
    # largest = getlargest(listan)
    # smallest = getsmallest(listan)
    smallest, largest, err = getLargestAndSmallest(listan)
#    smallest, largest, err = getLargestAndSmallest([])
    if err == "":
        print(f"{smallest} {largest}")
    else:
        print(err)


if __name__ == "__main__":
    mainDecorator()
    mainFuncGen()
    mainFunc()
    mainMultiParams()
    mainHockey()
    main()
