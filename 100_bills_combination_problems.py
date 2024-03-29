#用暴力的方法解决各种面额的硬币组成100圆的方法
import itertools as it
bills = [20, 20, 20, 10, 10, 10, 10, 10, 5, 5, 1, 1, 1, 1, 1]
make_100 = []
for n in range(1,len(bills)+1):
    for c in it.combinations(bills,n):
        if sum(c) == 100:
            make_100.append(c)
print(set(make_100))

bills = [50, 20, 10,5,1]
make_100 = []
for n in range(1, 101):
    for combination in it.combinations_with_replacement(bills, n):
        if sum(combination) == 100:
            make_100.append(combination)
print(set(make_100))

