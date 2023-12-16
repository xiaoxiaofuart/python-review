"""
      字典的遍历有多种方式：
        1）for key in dict 直接遍历相当于遍历key
        2）for entry in dict.items 遍历的是字典的内容，返回的是元组类型，获取key为 entry(0),获取value为 entry(1)
        3）for key  in dict.keys 遍历的是key
        4） for value in dict.values 遍历的是value
     字典的解析分为 与list 类似，
      1） {key:value for key,value in dictt.items} 不带条件的解析
      2） {key:value for key,value in dict.items if condition} 带条件的字典解析
"""

dict_student = {
    "name": "Jack",
    "age": 15,
    "hobbit": ['movie','music']
}

for key in dict_student:
    print("循环列表1："+key)

for entry in dict_student.items():
    # 返回的是个元组
    print("循环列表2："+entry[0]+"值为："+str(entry[1]))


for key in dict_student.keys():
    print(f"循环列表3：{key}")

for value in dict_student.values():
    print(f"循环列表4：{value}")


dict_student1 = {
    "sex": "male",
    "name": "Tom"
}


# 列表进行合并,存在相同的key，值会被最后一个字典中的key覆盖
print({**dict_student, **dict_student1})
print({**dict_student1, **dict_student})


# 字典解析
print({key: "new" + str(value) for key, value in dict_student.items()})
# 带if条件的字典解析
print({key: value for key, value in dict_student.items() if key != 'name'})

