from math import *
from decimal import *
def methoda(a):
    n = 0
    getcontext().prec = 1000
    total = Decimal(0)
    for i in range(1):
        for a in range(a):
            total = Decimal(total) + Decimal(1/Decimal(factorial(n)))
            n = n + 1
        print(Decimal(total))

a = 5000
methoda(a)
