# split each line pn the space
# 


def passChecker():
    numValidPass = 0
    with open('day-2\day-2-inpt.txt') as file:
        for line in file:
            store = line.split(' ')
            lowVal = int(store[0].split('-')[0])
            highVal = int(store[0].split('-')[1])
            letter = store[1].split(':')[0]
            passGiven = store[2]
            finds = 0
            for char in passGiven:
                if char == letter:
                    finds += 1
            if finds <= highVal and finds >= lowVal:
                numValidPass += 1
    return numValidPass

def newPassChecker():
    numValidPass = 0
    with open('day-2\day-2-inpt.txt') as file:
        for line in file:
            store = line.split(' ')
            numRange = store[0]
            lowVal = int(numRange.split('-')[0]) 
            highVal = int(numRange.split('-')[1])
            letter = store[1].split(':')[0]
            passGiven = store[2]
            firstLet = passGiven[lowVal - 1]
            secondLet = passGiven[highVal - 1]
            if (letter == firstLet) ^ (letter == secondLet):
                numValidPass += 1
    return numValidPass
            
print(passChecker(), newPassChecker())

