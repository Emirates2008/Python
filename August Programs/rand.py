from random import *

def generateAccountNumber(bankname):
    alpha="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    alphalist=list(alpha)
    shuffle(alphalist)
    a=str(randrange(100000,999999))
    print(a)
    onenum=int(a[0:1])
    twonum=int(a[1:2])
    threenum=int(a[2:3])
    fournum=int(a[3:4])
    fivenum=int(a[4:5])
    sixnum=int(a[5:6])
    b=alphalist[onenum]
    c=alphalist[twonum]
    e=alphalist[threenum]
    f=alphalist[fournum]
    g=alphalist[fivenum]
    h=alphalist[sixnum]
    d=b+c+e+f+g+h
    return bankname+str(a)+str(d).upper()
        
def validatePhoneNum(phonenum):
    if len(str(phonenum)) is 10:
        return True
    else:
        return False
def validateAge(age):
    if int(age)>18:
        return True
    else:
        print("You are two small to get bank account")
        return False

def CreateAccount(name,phonenum,country,age):
        print(validatePhoneNum(phonenum))
        print(validateAge(age))
        if(validatePhoneNum(phonenum) and validateAge(age)):
            Account_number=generateAccountNumber("UB")
            balanceamount = 0
            return [Account_number,name,phonenum,age,country,balanceamount]
        else:
            print("Please provide your real identity")
            return None


def WriteToFile(fname,account_details):
    f=open(fname,'w')
    f.write(account_details)
    f.write("\n")
    f.close()

name = input("Enter your FULL name.")
phonenum = int(input("Enter your phone number without -'s."))
country  = input("Enter the name of your country.")
age = int(input("Please enter your age."))
account_details=CreateAccount(name,phonenum,country,age)
if account_details is not None:
    WriteToFile("bankaccounts.txt",str(account_details))




    
    
    


