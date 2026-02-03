# Default arguements are the default value we provide while creating the function. This way the function assumes a default value even if the value is not provided in the function call for that arguement.


def avg (a=10,b=20): #here a and b are the default arguements 
    average=(a+b)/2
    print(average)
avg()
