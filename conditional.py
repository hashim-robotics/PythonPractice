# Product of two number Print even, odd, or zero 

import sys

def func(x,y):
    x = int(x)
    y = int(y)
    
    c= x*y;
    
    if(c==0):
        print("zero")
    elif (c%2 == 0):
        print("even")
    else:
        print("odd")

func(sys.argv[1],sys.argv[2])
    