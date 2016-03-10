__author__ = 'asuspc'


import random
import unittest


def rand5():
    return random.randint(0,4)


class program():

    table = ((0,1,2,3,4),
             (5,6,0,1,2),
             (3,4,5,6,0),
             (1,2,3,4,5),
             (6,7,7,7,7))

    def __init__(self):
        pass

    def rand7(self):
        x = rand5()
        y = rand5()
        if y == 4 and x > 0:
            return self.rand7()
        result = self.table[y][x]
        return result


class TestStringMethods(unittest.TestCase):
    def test_rand7_equally_division(self):
        gen = program()

        set = {0 : 0, 1:0, 2 :0, 3: 0, 4: 0, 5: 0, 6 :0}
        #fill set
        for x in range(1000):
            num = gen.rand7()
            set[num] += 1

        #print set
        for x in set:
            print(str(x) + ' count: ' + str(set[x]))

        #check spread
        diff = 70

        counts = list([set[x] for x in set])
        counts.sort()
        self.assertTrue(counts[0] > counts[-1] - diff)


if __name__ == '__main__':
    unittest.main()