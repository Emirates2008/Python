# A program to print all the numbers divisible by 21 between 100 and 2000.
def Div21():
    '''Divisors of 21'''
    for a in range(1000,2000):
        '''checking the num from 1000 and 2000'''
        if (a%21==0):
            '''checking if remainder is 0 when divided by 21'''
            print(a) # Print The number


