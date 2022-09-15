import random

def piEstimation(n):
    totalpts = 0
    circlepts = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        if (x**2+y**2) <= 1:
            circlepts+=1
        totalpts+=1
    return 4*(circlepts/totalpts)

while(True):
    number = int(input('enter a number of points: '))
    print(piEstimation(number))
