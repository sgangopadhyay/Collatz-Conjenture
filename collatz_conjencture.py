# NAME : Suman Gangopadhyay
# PROGRAM : Python program for Collatz Conjecture
# DATE : 27-June-2022
# VERSION : 1
# CAVEATS : None

def Collatz_Conjenture(number):
    '''A Python Function for Collatz Conjenture also known by 3n+1 Problem'''
    result = [number]
    while(number > 1):
        if(number % 2):
            number = (3*number)+1
            result.append(number)
        else:
            number = number//2
            result.append(number)
    return result
