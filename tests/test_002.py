'''
 Project: MPG Desktop Application
 Module:  test_001.py
 
 Description: 
 This is a test script for the Gas Desktop Application  


 Name          Date         Issue   
 R. Gaisey   12/29/23    initial commits 

 '''

import unittest
import os

class TestGeneric(unittest.TestCase):

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_string2(self):
        a = 'not some'
        b = 'not some'
        self.assertEqual(a, b)

if __name__ == '__main__':
    unittest.main()



