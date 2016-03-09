__author__ = 'asuspc'

def is_palindrome(input, i):
    if i >= len(input) // 2:
        return True
    return is_palindrome(input, i+1) and input[i] == input[-(i+1)]

r = ''
while r != 'exit':
    r = input()
    print(str(is_palindrome(r, 0)))