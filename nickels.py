__author__ = 'asuspc'


quarter = 25
dime = 10
nickel = 5
pennie = 1

options = 0

def printOptions():
    print(str(options))

def addOption():
    global options
    options += 1

def chunk(amount, divided):

    if amount - quarter > -1 and (len(divided) < 1 or divided[-1] > dime):
        stack = divided[:]
        stack.append(quarter)
        chunk(amount - quarter, stack)

    if amount - dime > -1 and (len(divided) < 1 or divided[-1] > nickel):
        stack = divided[:]
        stack.append(dime)
        chunk(amount - dime, stack)

    if amount - nickel > - 1 and (len(divided) < 1 or divided[-1] > pennie):
        stack = divided[:]
        stack.append(nickel)
        chunk(amount - nickel, stack)

    if amount - pennie > -1:
        stack = divided[:]
        stack.append(pennie)
        chunk(amount - pennie, stack)

    else:
        #no more money to split
        addOption()
        print(divided)

chunk(25, [])
printOptions()

