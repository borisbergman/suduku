__author__ = 'asuspc'

#solve any sudoku puzzle

import math

orig   = ((0,0,0,2,0,6,0,0,3),
         ( 0,6,0,0,8,0,0,0,0),
         ( 0,7,1,0,0,3,0,0,0),

          (0,0,6,0,0,0,9,1,0),
          (0,0,7,8,0,9,6,0,0),
          (0,2,4,0,0,0,8,0,0),

          (0,0,0,1,0,0,5,4,0),
          (0,0,0,0,3,0,0,8,0),
          (2,0,0,6,0,8,0,0,0))

copy = [list(row[:]) for row in orig]

stack = []

index = 0


def build_stack():
    tracking = [(x,y) for x in range(len(orig)) for y in range(len(orig))]
    for num in tracking:
        if orig[num[0]][num[1]] == 0:
            stack.append(num)


def solve_it():
    global index
    #print("solving for: " + str(index))
    #print("row: " + str(stack[index][0]) + " column: " + str(stack[index][1]) + " number: " + str(copy[stack[index][0]][stack[index][1]]))

    while True:
        copy[stack[index][0]][stack[index][1]] += 1
        if copy[stack[index][0]][stack[index][1]] > 9:
            copy[stack[index][0]][stack[index][1]] = 0
            #backtrack
            index -= 1
            return
        if validate():
            index += 1
            return


def check_columns():
    for column in range(len(orig[0])):
        column_nums = [k[column] for k in copy if k[column] > 0]
        col_count = len(set(column_nums))
        if col_count < len(column_nums):
            return False
    return True


def check_rows():
    for row in range(len(orig)):
        row_nums = [x for x in copy[row][:] if x > 0]
        row_count = len(set(row_nums))
        if row_count < len(row_nums):
            return False
    return True


def check_squares():
    squared = int(math.sqrt(len(orig)))
    to_check = [(x*squared, y*squared, squared) for x in range(squared) for y in range(squared)]
    for x in to_check:
        if not check_square(x[0], x[1], x[2]):
            return False
    return True


def check_square(top,left, count):
    values = [x[left:left+count] for x in copy[top:top+count]]
    list = [x for t in values for x in t if x > 0]
    if len(set(list)) < len(list):
        return False
    return True


def solve_stack():
    global index
    while len(stack) > index:
        solve_it()


def validate():
    return check_columns() and check_rows() and check_squares()
#increment()

build_stack()
solve_stack()

for row in copy:
    print(row)

print (validate())

