# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 13:44:00 2016
Updated Jan 21, 2018

The primary goal of this file is to demonstrate a simple python program to classify triangles

@author: jrr
@author: rk

-------------------

NOTE: The original code with intentional bugs was written by the above authors^. I have commented out the original 
buggy code in the first part of the function to show the original code with its bugs before I edited. 
Below that, I have copy and pasted the buggy code and edited it to remove the bugs that I found. 

@author: amanda-zambrana
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code

---------------

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= b or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if (a >= (b - c)) or (b >= (a - c)) or (c >= (a + b)):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if a == b and b == a:
        return 'Equilateral'
    elif ((a * 2) + (b * 2)) == (c * 2):
        return 'Right'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
    else:
        return 'Isoceles'

    """

    # require that the input values be > 0 and <= 200 (need to be greater than 0, not greater or equal)
    if a > 200 or b > 200 or c > 200:  
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:  # here, I change 'b <= b' to 'b <= 0' to avoid invalid input for any b
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    # NOTE: I did not change anything here, even though sides of triangle do not have to be integers only, 
    # but I figured this was preference for the code, not a bug 
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):  
        return 'InvalidInput'
      
    # The original logic here noted in the comments was incorrect according to the triangle inequality theorem. 
    # It stated that the sum of any two sides must be strictly less than the third side, but this is wrong. Instead,
    # it it that the sum of any two sides must be GREATER than the third side 
    # So, I changed the logic to reflect that and removed the 'or equal to' symbols & made sure it was 
    # the sum of any two sides rather than the difference of any two sides 
    if (a > (b + c)) or (b > (a + c)) or (c > (a + b)):  
        return 'NotATriangle'
        

# now we know that we have a valid triangle, so we can classify into which types of triangle 

    # all three sides must be equal for an equilateral, so I changed that here to include a,b, and c (not only a and b)
    if a == b and b == c:  
        return 'Equilateral'
    # For right triangles, we use the pythagorean theorem (a^2 + b^2 = c^2) and apply for any combo of sides.
    # Here, the bug is that it used multiplication (*) instead of square (**) and only did it for one combination. 
    elif ((a**2) + (b**2)) == (c**2) or ((b**2) + (c**2)) == (a**2) or ((a**2) + (c**2)) == (b**2):
        return 'Right'
    # here, I changed the final condition to be (a != c) because none of the 3 sides can be equal in a scalene
    elif (a != b) and  (b != c) and (a != c):
        return 'Scalene'
    else:
        return 'Isosceles'  # there was a typo here in the original code, so i fixed that bug here!
    

