import random
count=[0,0]
for i in range(10000):
    toss_result=random.randint(0,1)
    count[toss_result]+=1
    
print("동전앞면의 확률",count[0]/10000)
print("동전뒷면의 확률",count[1]/10000)  
