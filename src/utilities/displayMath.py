'''
 Project: MPG Desktop Application
 Module:  displayMath.py
 
 Description: 
 This module contains utility functions related to displaying values in the application

 
 Name          Date     Issue   
 R. Gaisey   11/1/23

 '''


def format_float(value, precision):
    return str( round(value, precision))