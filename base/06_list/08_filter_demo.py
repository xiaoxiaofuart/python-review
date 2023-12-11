

list_num = [1, 5, 6, 4]

print(list(filter(lambda num_item: num_item > 4, list_num)))

list_tuple = [('jack', 22), ('hellon', 5)]

print(list(filter(lambda tuple_item: tuple_item[1] > 8, list_tuple)))

