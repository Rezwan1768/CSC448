# Rezwan Ahmed
# 10/31/2023

import math

for number in range(3, 101): # loop from 3 to 100
    initial_divisor = math.isqrt(number)
    isPrime = True

    for divisor in range (initial_divisor, 1, -1):
        if(number % divisor == 0):
            print(str(number) + ":\tNot prime")
            isPrime = False
            break

    if(isPrime):
        print(str(number) + ":\tPrime")