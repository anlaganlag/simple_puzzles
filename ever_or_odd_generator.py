def even():
    start=0
    while True:
        yield start
        start += 2
        
def odd():
    start=1
    while True:
        yield start
        start += 2
g1=even()
g2=odd()
print(next(g1))
print(next(g2))


import itertools as it
evens = it.count(step=2)
odds = it.count(start=1,step=2)
l1=list(next(evens) for _ in  range(5))
l2=list(next(odds) for _ in  range(5))
print(l1)
print(l2)

count_with_floats = it.count(start=0.5, step=0.75)
list(next(count_with_floats) for _ in range(5))
#[0.5, 1.25, 2.0, 2.75, 3.5]

negative_count = it.count(start=-1, step=-0.5)
list(next(negative_count) for _ in range(5))
#[-1, -1.5, -2.0, -2.5, -3.0]

