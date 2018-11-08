import random
#from random import*
import math

n=int(input("반복횟수는:"))
inside=0
for i in range(n):
    x=random.random()
    y=random.random()
    if math.sqrt(x**2+y**2)<=1:
        inside+=1

Pi=4*inside/n
print("원주율은",Pi)
