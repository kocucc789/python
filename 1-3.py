import random
inside=0
n=int(input("반복횟수는"))
for i in range(10000):
    x=random.random()
    y=random.random()
    if y<=x:
        inside+=1

print("삼각형의 면적은",inside/10000*1)        
