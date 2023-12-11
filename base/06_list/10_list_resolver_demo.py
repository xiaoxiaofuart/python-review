"""
    python中可以对列表进行解析，将结果输出为一个新的列表，也可以带条件
"""

list_num = [1, 2, 3, 4]

print([item ** 2 for item in list_num])
#   带条件的列表解析
print([item ** 2 for item in list_num if item > 3])
