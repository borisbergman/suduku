__author__ = 'asuspc'

import unittest

#find loop in linked list



class node():
    def __init__(self, number):
        self.next_node = None
        self.number = number

    def set_next(self, next_node):
        self.next_node = next_node

linked_list = node(0)

def create_list():
    p = linked_list

    for x in range(10):
        h = node(x+1)
        p.next_node = h
        p = h

    #make circle by point last node to 3rd node
    p.next_node = n.next_node.next_node.next_node

class TestStringMethods(unittest.TestCase):
    def find_loop(self):

        fast_iterator = linked_list
        slow_iterator = linked_list

        while True:
            if slow_iterator.next_node is not None:
                slow_iterator = linked_list.next_node
            else:
                print("no loop")
                return
            if fast_iterator.next_node is not None:
                if fast_iterator.next_node.next_node is not None:
                    fast_iterator= linked_list.next_node.next_node
                else:
                    print("no loop")
                    return
            if slow_iterator == fast_iterator:
                print("collision. Loop detected")



if __name__ == '__main__':
    create_list()
    unittest.main()