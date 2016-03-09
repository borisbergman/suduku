__author__ = 'asuspc'


def parantesis(n, are_open, stack):

    #open path
    if n - are_open > 0:
        st1 = stack[:]
        st1.append("(")
        parantesis(n-1, are_open+1, st1)
    #close path
    if are_open > 0:
        st2 = stack[:]
        st2.append(")")
        parantesis(n-1, are_open-1, st2)

    if n < 1:
        print(stack)

parantesis(6, 0, [])