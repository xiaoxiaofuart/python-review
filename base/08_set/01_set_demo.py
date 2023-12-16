"""
    python中的set集合里面元素不允许为相同
    1.定义一个set {1,2,3},定义一个空set set = set()
    2.添加元素 set.add()
    3.修改不了set
    3.查询一个元素是否在set中, value in set
    4.删除一个set 1)set.discard(‘value’) 2) set.remove(‘value’) 3) set.pop
     第一个和第二个都可以删除一个指定元素，区别就是remove删除一个不存在的元素会报错，第三个是随机弹出一个元素博并从原始set中删除此元素
"""

set_demo = {1, 2, 3}
# 定义个空的set集合
set_empty = set()

# 判断一个元素是否存在set中
print(1 in set_demo)

set_demo.add(5)
print(set_demo)

# 删除一个不存在的元素会报错
# set_demo.remove(6)

# 删除一个不存在的元素返回 None,不会报错
set_demo.discard(5)
print(set_demo)

# 随机取出一个元素
print(set_demo.pop())
