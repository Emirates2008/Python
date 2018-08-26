from banking_functions import *
import sys
while True:
    print(" 1. Create Account\n")
    print(" 2. Display Balance\n")
    print(" 3. Credit(add)Money\n")
    print(" 4. Debit(withdraw)Money\n")
    print(" 5. Exit United Bank\n")
    a = int(input("Choose a option from the ones above. Enter 1,2,3,or 4."))
    if (a == 1):
        Input_Account_Creation()
    elif (a == 2):
        display_Balance()
    elif(a == 3):
        ## Add money to  the account
        add_Money()
    elif(a == 5):
        ##Exit fromt the program
        sys.exit(0)
    else:
         print("No such choice.")   
        
