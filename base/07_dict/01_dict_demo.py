"""
    python 中map是一个键值对，其中key是不允许重复的
    1.根据key获取元素 dict['key'] 或者 dict.get(key) 两者的区别是 dict['key']当key不存在的时候程序会报错，而 dict['key']会返回none
    2.添加key   dict【‘key’】 = value
    3.修改key   dict【‘key’】 = new_value
    4.删除key    del  dict【‘key’】
"""


dict_student = {
    "name":"tom",
    "age":11,
    "hobbit":['basekeball','football','song']
}

print("学生的姓名为："+dict_student['name'])

print("学生的年龄为："+str(dict_student.get('age')))


# dict_student['sex'] 会报错

# dict_student.get('sex') 输出为None


dict_student['sex'] = "male"
print(dict_student['sex'])

dict_student['sex'] = 'female'
print(dict_student['sex'])


del dict_student['name']


print(dict_student)


