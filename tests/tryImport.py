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
import .src.utilities 
import .src.gasMain

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
    appInstance = gasMain.SummaryWindow.dv
    '''
    print(f" Estimated Range:  {format_float(dv.get_est_range(), 2)} Mileage {format_float(dv.get_est_mileage(), 2)} \n \
        Overall Mileage {format_float(dv.get_overall_mileage(), 2)} MPG: {format_float(dv.get_overall_mpg(), 2)} \n \
        Recent Mileage {format_float(dv.get_recent_mileage(), 2)} MPG: {format_float(dv.get_recent_mpg(), 2)}\n \
        Completed packet")
    '''

    print(f" Estimated Range:  {appInstance.get_est_range()} Mileage {appInstance.get_est_mileage()} \n \
    Overall Mileage {appInstance.get_overall_mileage()} MPG: {appInstance.get_overall_mpg()} \n \
    Recent Mileage {appInstance.get_recent_mileage()} MPG: {appInstance.get_recent_mpg()}\n \
    Completed packet")
    
    



