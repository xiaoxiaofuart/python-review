"""
    python 中排序有两种方式
    1.使用list自带的sort函数支持排序，此排序会更改list的元素顺序，排序方法中可以指定排序的key
    2.使用全局函数sorted进行排序，此排序不会改变原list结果，返回一个新的list，同样可以使用指定key或者倒序的方式进行排序
"""

list_num = [5, 2, 6, 7, 8]
list_num.sort()
print(list_num)
list_num.sort(reverse=True)
print(list_num)  # 倒序

list_tuple = [('xiaoming', 12), ('xiaohong', 5), ('xiaowang', 8), ('xiaozhang', 22)]
#   指定排序key为元组中的第二个元素
list_tuple.sort(key=lambda stu: stu[1])
print(list_tuple)


list_new = sorted(list_num)
print(list_new)



