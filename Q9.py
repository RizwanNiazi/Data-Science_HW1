#------------Q9--------
import Tuple
print("Enter Character if you want to do Operation with tuple ?")
print("Enter A if you want to do the addition")
print("Enter S if you want to do the Substraction") 
print("Enter M for multiplication")
print("Enter D for Division ")
print("Enter P for power")
a=input("")
tup=(10,3)
p1=Tuple.tuple(10,3)
if a=='A':
    p1.Addition(tup)
elif a=='S':
    p1.Subtraction(tup)
elif a=='M':
    p1.Multiplication(tup)
elif a=='D':
    p1.Division(tup)
elif a=='P':
    p1.Power(tup)
else: # default, could also just omit condition or 'if True'
    print("something else!")
