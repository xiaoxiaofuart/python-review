raw_str = r" this is \"原生\""
raw_str1 = " this is \"转义\""

print(raw_str)  # this is \"原生\"
print(raw_str1)  # this is "转义"


hello_world = "hello world"

# 截取字符串，不包含最后一个下标
print(hello_world[0:2])
# 判断是否小写
print(hello_world.islower())
# 获取字符串的长度
print(hello_world.__len__())

# 统计某个字符出现的次数
print(hello_world.count("l"))
# 判断某个字符串是否以hell 开头
print(hello_world.startswith("hell"))

#从左往右匹配字符串，返回第一个匹配的索引
print(hello_world.find("l"))
#从右往左匹配字符串，返回第一个匹配的索引
print(hello_world.rfind("l"))

# 字符串翻转
print("".join(reversed(hello_world)))
print(hello_world[::-1])

# 按照一定的步长提取字符串
print(hello_world[::3]) # hlwl

str_1 = "1"

print(type(int(str_1)))
# 判断一个变量是否属于某个类型
print(isinstance(str_1,int)) # False



