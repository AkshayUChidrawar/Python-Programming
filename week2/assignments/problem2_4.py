import random
def problem2_4():
    random.seed(70)                 
    num = []
    for each in range (0, 10):
        b = random.random()*5
        n = 30 + b
        num.append(n)
    print (num)