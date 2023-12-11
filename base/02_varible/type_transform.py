# python 中支持类型转换，常见的类型转换函数如下
# str(a) 将a转换为string
# int(a) 将a转换成 int
# float(a) 将a转换成一个浮点类型
# boolean(a) 将转换成一个布尔类型

a = '1'
b = '2'
print(int(a) + int(b))  # 3

print(float(a) + float(b))  # 3.0

c = 1
d = 1
print(str(c) + str(d))  # 11

e = 0  # false
f = 1  # true

print(bool(e))
print(bool(f))
