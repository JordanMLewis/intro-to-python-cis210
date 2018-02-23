'''
    Author: Jordan Mitchell Lewis
    Date: 02/08/16
    Class: CIS 210, Winter 2016
    Credits:
    This file contains functions that reverse a string using either recursive or iterative methods.
'''

import doctest

def strReverseR(s):
    '''
    (string) ---> string

    strReverseR takes an input s as a string, and uses a recursive
    solution to reverse the string. It will return the inputted string
    in reversed order.
    
    >>>strReverseR('CIS 210') 
    '012 SIC'

    '''
    if s == "":
        return s 
    else:
        return strReverseR(s[1:]) + s[0] #solve for the s from index 1 to end, and add whatever is before it (s[0])
            
def strReverseI(s):
    '''
    (string) ---> string

    strReverseI takes an input s as a string, and uses a iterative
    solution to reverse the string. It will return the inputted string
    in reversed order.
    
    >>>strReverseI('CIS 210') 
    '012 SIC'

    '''
    reverseStringI = s[::-1] #[begin:end:step], no beginning or end, so it steps backwards and reverses the s
    return reverseStringI

def strReverseR_stub(s):
    '''
    (string) ---> string

    strReverseR takes an input s as a string, and uses a recursive
    solution to reverse the string. It will return the inputted string
    in reversed order.
    
    >>>strReverseR('CIS 210') 
    '012 SIC'

    '''
    pass
    return None

def strReverseI_stub(s):
    '''
    (string) ---> string

    strReverseI takes an input s as a string, and uses a iterative
    solution to reverse the string. It will return the inputted string
    in reversed order.
    
    >>>strReverseI('CIS 210') 
    '012 SIC'

    '''
    pass
    return None

