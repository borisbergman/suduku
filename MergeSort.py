from collections import deque

unsorted = [14, 7, 3, 12, 9, 11, 6, 2, -9, -3, 88, 101, 0]

# merge 2 arrays together


def merge(array, p, q, r):
    a = array[p:q+1][::-1]
    b = array[q+1:r+1][::-1]
    x = 0
    while a and b:
        if a[-1] < b[-1]:
            array[x + p] = a.pop()
        else:
            array[x + p] = b.pop()
        x += 1

    while a:
        array[x+p] = a.pop()
        x += 1
    while b:
        array[x+p] = b.pop()
        x += 1


def merge_sort(array, p, r):
    if(r-p) > 0:
        q = (r-p)//2+p
        merge_sort(array, p, q)
        print("merge 1 " + str(p) + "-" + str(q))
        merge_sort(array, q+1, r)
        print("merge 2 " + str(q+1) + "-" + str(r))
        merge(array, p, q, r)

merge_sort(unsorted, 0, len(unsorted)-1)

[print(x) for x in unsorted]