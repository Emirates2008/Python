#
def Grade():
    p = input("What is your name?")
    sub1 = input("Enter a subject that you want to be graded on.")
    mark1 = int(input("What is your marks for this subject?"))
    sub2 = input("Enter anohter subject that you want to be graded on.")
    mark2 = int(input("What is your marks for this subject?"))
    sub3 = input("Enter another subject that you want to be graded on.")
    mark3 = int(input("What is your marks in this subject?"))
    sub4 = input("Enter another subject that you want to be graded on.")
    mark4 = int(input("What is your marks for this subject?"))
    sub5 = input("Enter another subject that you want to be graded on.")
    mark5 = int(input("What is your marks for this subject?"))
    t = mark1 + mark2 + mark3 + mark4 + mark5
    t = int(t)
    t = (t*100)//500
    if(t > 90):
        print ("Your grade is an A!")
    
    elif(t > 80 and t < 90):
        print ("Your grade is a B.")
    
    elif(t > 80 and t <70):
        print ("Your grade is a C.")

    elif(t > 60 and t < 70):
        print ("Your grade is an D.")
    
    elif(t > 50 and t < 60):
        print ("Your grade is an E.")    
    
    elif(t < 50):
        print ("Your grade is an F.")
