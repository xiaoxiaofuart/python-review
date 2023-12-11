a = True
a = "5"
print(a)

# 定义一个字符串
a = "I love study"
for a1 in a:
    print("====", a1)

# 定义一个元组
a = (1, 2, 3)

# 定义只包含一个元素的元组
turple1 = (3,)

# 定义一个空元组，用处是啥？1.函数返回多个值时使用空元组 2.表示空序列时使用空元组 3.作为占位符使用
turple1 = ()

for b in a:
    print("=======", b)
# 获取第一个元素
print(a[0])
# 元组的值不能改变，如果时list,则可以添加list里面元素
#a[0] = 2
#01_print(a[0])

a = (1, 2, [4, 5])
list1 = a[2]
list1.append("3")
print("==向元组中的列表添加元素==", list1)


# 定义列表
listA = [1, 2, 3, 4]
for index, list1 in enumerate(listA):
    print("列表中第{}元素是{}".format(index, list1))


# 定义set
set1 = set([1, 2, 3, 2])
print(set1)



#  定义字典
dict1 = {"name": "tom", "age": 18, "school": "hefei"}
print(dict1)
print(dict1['name'])
print(dict1['jieke'])

