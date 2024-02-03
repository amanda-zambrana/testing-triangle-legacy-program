# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

--------------------

NOTE: The first three tests were written by the above authors^ . The following tests I added as 
enhancements to this test code. 

@author: amanda-zambrana
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    # We should add a test for isosceles triangles 
    def testIsoscelesTriangle(self):
        self.assertEqual(classifyTriangle(2,2,3), 'Isosceles', '2,2,3 is an Isosceles triangle')
        
    # Next we should add a test for scalene triangles 
    def testScaleneTriangle(self):
        self.assertEqual(classifyTriangle(3,4,6), 'Scalene', '3,4,6 is a Scalene triangle')

    # We can also add a test to make sure that the 3 sides make a triangle
    def testNotATriangle(self):
        self.assertEqual(classifyTriangle(1,1,12), 'NotATriangle', '1,1,12 is Not A Triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

