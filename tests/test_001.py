'''
 Project: MPG Desktop Application
 Module:  test_001.py
 
 Description: 
 This is a test script for the Gas Desktop Application  

 Name          Date         Issue   
 R. Gaisey   12/29/23    initial commits 

 '''

import unittest

#import gasMain
#import utilities
import utilities 
import gasMain



class TestGasApp(unittest.TestCase):

    def test_string(self):
        a = 'some'
        b = 'some'
        self.assertEqual(a, b)

    def test_boolean(self):
        a = True
        b = True
        self.assertEqual(a, b)

    def test_importExists(self):
        variable = 15
        self.assertIsNotNone(variable)

    def test_AppExists(self):
        app = 5
        self.assertIsNotNone(app)

if __name__ == '__main__':
    unittest.main()