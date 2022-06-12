# -*- coding: utf-8 -*-
"""
Created on Sun Jun 12 19:02:41 2022

@author: sdutta
"""
import unittest

from BMI import BMI_add
        
class BMITestCase(unittest.TestCase):
    
    def test_BMIcategory(self):
        BMI, BMI_Category, Health_Risk = BMI_add(96, 1.71) 
        actual = BMI
        expected = 32.83
        self.assertEqual(actual, expected)
    

