#Functions are used to seperate the logic.


def addition(a,b): # here a,b are arguements
    added_value=a+b
    print(added_value)

def isGreater(a,b):
    if a > b :
        print ("a is greater than b")
    else :
        print("b is gretaer than a")

a=35
b=27
addition(a,b) #calling the function
isGreater(a,b) #calling the function

c=78
d=45
addition(c,d) #calling the function for different variables
isGreater(c,d) #calling the funtion for different variables 