'''
    Author: Jordan Mitchell Lewis
    Class: CIS 210, Winter 2016
    Date: 01/11/2016
    This file contains a function that determines the estimated temperature based on cricket chrips.
'''

from temperature import ctemp_to_ftemp

def chirps_to_ftemp(c25):
    '''
    (number) -> (float)

    The function will take an input as the number of cricket chirps
    within 25 seconds and will return a temperature in Fahrenheit.

    Ex:
    chirps_to_ftemp(48) would evaluate to 68.0 degrees Fahrenheit.
    chirps_to_ftemp(str) would produce an error.
    '''
    print('The estimated Fahrenheit temperature is:', (ctemp_to_ftemp((c25 / 3) + 4)), 'degrees.')

def chirps_to_ftemp_stub():
    '''
    (number) -> (float)

    The function will take an input as the number of cricket chirps
    within 25 seconds and will return a temperature in Fahrenheit.

    Ex:
    chirps_to_ftemp(48) would evaluate to 68.0 degrees Fahrenheit.
    chirps_to_ftemp(str) would produce an error.
    '''
    pass
    print #ftemp
