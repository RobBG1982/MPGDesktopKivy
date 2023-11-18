'''
 Project: MPG Desktop Application
 Module:  displayMath.py
 
 Description: 
 This module contains utility functions related to displaying values in the application

 
 Name          Date          Issue   
 R. Gaisey   11/01/23    
 R. Gaisey   11/18/23    added rgb conversion function

 '''


def format_float(value, precision):
    return str( round(value, precision))

def get_rgb(v1):
    return v1/255