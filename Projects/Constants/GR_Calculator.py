import math
from decimal import *

def golden():
    getcontext().prec = 100
    gr = Decimal(1+Decimal(math.sqrt(Decimal(5))))/2
    return gr

print(golden())
