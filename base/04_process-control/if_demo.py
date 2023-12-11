"""
    python中 条件表达式为 if 表达式： elif 表达式： else:
    三元表达式 值1 if 表达式 else 值2 满足表达式，结果返回值1，否则返回值2
"""

a = input("请输入一个数字：")

num = int(a)

if num > 10:
    print(r"I'm bigger")
elif 10 >= num > 0:
    print(r"I'm middle")
else:
    print("I'm smaller")


# 三元表达式

str1 = "yes" if num > 10 else 'no'

print(str1)
