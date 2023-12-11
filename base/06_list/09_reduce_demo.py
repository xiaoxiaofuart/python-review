from functools import reduce

list_num = [1, 2, 3, 4, 5]

print(reduce(lambda item1, item2: item1 + item2, list_num))