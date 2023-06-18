import random as rd
import math

# ============================================================================ #

X = [0.1 * x for x in range(100)]

# ============================================================================ #

with open("linear.csv", "w") as hlinear :
    Y = [2 * x + rd.uniform(-0.5, 0.5) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)

# ---------------------------------------------------------------------------- #

with open("cubic.csv", "w") as hlinear :
    Y = [0.1 * (x - 1) * (x - 4) * (x - 7) + rd.uniform(-0.5, 0.5) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)

# ---------------------------------------------------------------------------- #

with open("exponential.csv", "w") as hlinear :
    Y = [10 * math.exp(-0.7 * x) + rd.uniform(-0.5, 0.5) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)

# ---------------------------------------------------------------------------- #

with open("sinoidal.csv", "w") as hlinear :
    Y = [3 * math.sin(1.5 * x + 1) + rd.uniform(-0.5, 0.5) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)

# ---------------------------------------------------------------------------- #

with open("gaussian.csv", "w") as hlinear :
    Y = [2 * math.exp(-2 * (x-4)**2 ) + rd.uniform(-0.05, 0.05) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)

# ---------------------------------------------------------------------------- #

with open("logarithmic.csv", "w") as hlinear :
    Y = [2 * math.log( 9 * x + 1 ) + rd.uniform(-0.5, 0.5) for x in X]
    
    for x, y in zip(X, Y) :
        print(x, y, sep=",", file=hlinear)
