__author__ = 'asuspc'


def swap(array, a, b):
    first = array[a]
    array[a] = array[b]
    array[b] = first


def partition(array, start, end):
    pivot = array[end]
    index = start
    for x in range(start, end):
        if array[x] <= pivot:
            swap(array, x, index)
            index += 1
    swap(array, index, end)
    return index


def quick_sort(array, p, r):
    if p < r:
        index = partition(array, p, r)
        quick_sort(array, p, index - 1)
        quick_sort(array, index + 1, r)


unsorted = [1, 99, 31, 12, 0, -1, 74, 17, 3]
quick_sort(unsorted, 0, len(unsorted) - 1)
[print(x) for x in unsorted]