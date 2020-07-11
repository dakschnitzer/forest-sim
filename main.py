import math
import random
import matplotlib.pyplot as plt
import numpy


ntrees = 1000
tree_x = numpy.zeros(ntrees) 
tree_y = numpy.zeros(ntrees) 
rad = [2, 2, 2, 2, 2, 4, 4, 4, 6, 6, 8]    

for i in range(ntrees - 1):
    if random.getrandbits(1) == 0:
        sign = 1
    else:
        sign = -1
        
    deg = math.radians(random.randint(0,359))

    tree_x[i + 1] = int(tree_x[i] + sign * random.choice(rad) * math.sin(deg))
    tree_y[i + 1] = int(tree_y[i] + sign * random.choice(rad) * math.cos(deg))


plt.scatter(tree_x, tree_y)
plt.show()