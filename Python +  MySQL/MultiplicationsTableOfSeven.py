def multiplication():
    FIXEDVALUE = 7
    count = 101

    for i in range(count):
        print(FIXEDVALUE * i, end=", ")
        i += 1
    print("Done using for loop")

multiplication()


def ShowTable():
    FIXEDVALUE = 7
    count = 101

    print("Your Output for the multiplication values of 7 is \n")
    for i in range(count):
        print(f"7 * {i} = {FIXEDVALUE * i}")
        i += 1
    print("Done using for loop table")
ShowTable()


def multiplicationusingwhile():
    FIXEDVALUE = 7
    count = 101
    i = 0

    while i < count:
        print(f"7 X {i}  = {FIXEDVALUE * i} \n")
        i += 1
    print("Done using while show tables")
multiplicationusingwhile()


def InputChoice():
    TableValue = int(input("Enter the table that you want to have : "))
    Count = int(input("How many counts : ")) +1
    StartValue = 1

    while StartValue < Count:
        print(f"{TableValue} X {StartValue}  = {TableValue * StartValue} \n")
        StartValue +=1
    print("Your multiplication table is high and done")
InputChoice()

