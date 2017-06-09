"""
https://stackoverflow.com/questions/44450197/newton-raphson-method-in-python/44450256?noredirect=1#comment75897751_44450256

I'm trying to calculate the approximated square root of a number in python using the Newton-Raphson method(The formula)



However the code does not work as it is stuck in the while loop(at least I think so). My plan is to calculate approximations until approximations differ by 1e–10. This is the code I have right now:

k = input("Enter a number")
try:
    k = int(k)
    xi = 1
    xi2 = xi - (xi**2 - k)/(xi*2)
    diff = xi2 - xi
    #0.0000000001
    while (diff > 0.0000000001):
        xi = xi2
        xi2 = xi - (xi**2 - k)/(xi*2)
        print(xi2)
    print(xi2)
except:
    print("bye")
I'm new to python so any help will be much appreciated! thanks a lot! :)

"""

#The while block didnt have a diff changer, I added it
#The author noted that the answers were wrong. 
#I figured that the program was dealing with differences, but not using absolute values. I added abs() to difference calculations and the problem was solved.
k = input("Enter a number ")
k = int(k)
xi = 1
xi2 = xi - (xi**2 - k)/(xi*2)
diff = abs(xi2 - xi)
#0.0000000001
while (diff > 0.0000000001):
    xi = xi2
    xi2 = xi - (xi**2 - k)/(xi*2)
    diff = abs(xi2 - xi)
    print(diff)
print(xi2)

