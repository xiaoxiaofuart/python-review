

dict_stu = {
    "name":"xiaoming",
    "age":16,
    "weight":"50kg"
}

print(dict_stu.get("name"))
print(dict_stu['name'])

dict_stu['sex'] = 'male'

for item in dict_stu.items():
    key = item[0]
    value = item[1]
    print(f'key为{key},value为{value}')


# 字典解析
for key,vlaue in dict_stu.items():
    print(f'字典的key为{key},字典的值为{value}')


# 字典合并
dict_person = {
    "hobbit":"football",
    'sex':'男'
}

# 字典合并，重复的键会以最后一条为准
dict_new = {**dict_stu,**dict_person}
print(dict_new)