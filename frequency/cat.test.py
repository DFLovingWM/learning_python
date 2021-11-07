# -*- coding: utf-8 -*-

from cat import countCat
import unittest


class TestMethod(unittest.TestCase):
    def testEmpty(self):
        animals = ['dog', 'lion', 'tiger', 'lion', 'mouse', 'giraffe']
        self.assertEqual(countCat(animals), 0)

    def testGeneral(self):
        animals = ['dog', 'lion', 'tiger', 'lion', 'cat', 'mouse', 'giraffe', 'little cat', 'cat']
        self.assertEqual(countCat(animals), 2)


if __name__ == '__main__':
    unittest.main()
