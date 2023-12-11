"""
    list操作：
    1.新增 ： insert(索引，值) 、append(值)在最后一位追加
    2.删除： del list[索引]、list.pop（）、list.remove(元素值)
    3.修改： list[索引] = 值
    4.查：list[索引]
"""

name_list = ['xiaoming','xiaohong','jack','tom']


print(name_list[0])
print(name_list[-1])

name_list[0] = 'xiugai'
print(name_list)

name_list.append("lastest")
name_list.insert(0,"lateste1")
print(name_list)

print(name_list.pop())
name_list.remove('xiaohong')
print(name_list)
del name_list[0]
print(name_list)

