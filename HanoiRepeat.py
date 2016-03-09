__author__ = 'asuspc'


peg1 = []
peg2 = []
peg3 = []

DiskAmount = 27;
count = 0

def FillPeg1():
    for x in range(DiskAmount, -1, -1):
        peg1.append(x)

def MoveDisk(Amount, From, To, SparePeg):
    global count
    count +=1
    if Amount == 0:
        x = From.pop()
        To.append(x)

    else:
        MoveDisk(Amount -1, From, SparePeg, To)
        x = From.pop()
        To.append(x)
        MoveDisk(Amount -1, SparePeg, To, From)

FillPeg1()

MoveDisk(DiskAmount-1, peg1, peg2, peg3)

[print(str(x)) for x in reversed(peg2)]
print("operations" + str(count))