"""
    map转换函数，不修改原集合数据 实现 type_a => type_b 的转换
    list函数可以接收一个iterator，将其转换为list
"""
list_num = [1, 2, 3, 4]
print(list(map(lambda item: 'str' + str(item), list_num)))

list_tuple = [('jack', 1), ('mary', 2), ('stone', 3)]
print(list(map(lambda tuple_item: tuple_item[1], list_tuple)))
