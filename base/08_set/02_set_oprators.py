"""
    python 中集合 涉及并集、交集等处理
    1.并集有两种处理方式 1）使用 set1.union(set2) 2）使用 | 符号进行并集处理 ，两者的区别就是 union 可以是非set集合，可以合并一个list或者tuple
    2.交接可以也有两种方式 1）使用 set1.intersection 2）第二种使用& 进行交集处理哦，区别同并集一样

    python中也涉及集合的解析
    1.基本的方式 {item  for item in set}
    2. 带if条件的解析 {item for item in set if condition}
"""

set_demo1 = {1, 2, 3}

set_demo2 = {3, 4}

list_demo1 = [2, 6]

# 可以与list进行求并集
print(set_demo1.union(list_demo1))

# 报错，|符号不支持非set集合的并集
# print(set_demo1 | list_demo1)
print(set_demo1 | set_demo2)

# 求并集,支持非set求并集
print(set_demo1.intersection(list_demo1))

print(set_demo1 & set_demo2)

# 报错，不支持非set的交集
# print(set_demo1&list_demo1)

# set基本解析
print({item*5 for item in set_demo1})

# set的带条件的解析
print({item*5 for item in set_demo1 if item > 1})

