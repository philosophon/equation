
import random


x=input("first number:")
y=input("second number:")
command=("multiplication","addition","division","subtraction")
multiplication=("multiply")
addition=("add")
subtraction=("subtract")
division=("divide")

while True:

    ask=input(">>>")
    if ask in multiplication:
        print(x*y)
    elif ask in addition:
        print(x+y)
    elif ask in division:
        print(x/y)
    elif ask in subtraction:
        print(x-y)
