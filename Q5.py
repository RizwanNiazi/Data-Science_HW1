
#-------------Q5------
for i in range(1,100):
    x=i
    if x%3==0 and x%5!=0:
        print("fizz")
    elif x%5==0 and x%3!=0:
        print("Buzz")
    elif x%3==0 and x%5==0:
        print("FizzBuzz")
    else:
        print(x)
