import random
def genPass():
    alphabet="abcdef"
    password=" "

    for i in range(6):
        index=random.randrange(len(alphabet))
        password=password+alphabet[index]
    return password

print(genPass())
print(genPass())
print(genPass())
