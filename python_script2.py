import itertools
from itertools import cycle
x = list(range(5))
for i, j in enumerate(cycle(x)):
    print(j, end = ' ')
    if i > 13:
        print()
        break


