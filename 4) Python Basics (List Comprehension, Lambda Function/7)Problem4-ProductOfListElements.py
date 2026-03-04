# Problem 4: Product of List: Use reduce to find product of all numbers in list.

from functools import reduce
numbers = [1,2,3,4,5]
product = reduce(lambda x,y: x*y, numbers)
print(product)