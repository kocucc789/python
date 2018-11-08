import random
count=[0,0]
n=int(input("동전던질 횟수는?:"))
for i in range(10000):
    toss_result=random.randint(0,1)
    count[toss_result]+=1
    
print("동전앞면의 확률",count[0]/n)
print("동전뒷면의 확률",count[1]/n)  
