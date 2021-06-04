with open ('day-4\day-4-inpt.txt') as file:
    for line in file:
        store = line.split("\n\n")
        store2 = [string.replace("\n", " ") for string in store]
        passports = [store2.split() for string in store2]
        print(passports)