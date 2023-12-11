
list_str = ['name', 'age', 'test']

# enumerate 可以使列表获取索引
for index, item in enumerate(list_str):
    print(f'{index} - {item}')

# 指定索引值从1开始
for index, item in enumerate(list_str, 1):
    print(f'{index} - {item}')


#   定义一个迭代器
it = iter(list_str)
for item in it:
    print(item)
