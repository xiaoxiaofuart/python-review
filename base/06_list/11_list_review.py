

list_stu1 = ['tom','alice','Jack']

print(list_stu1[0])

print(list_stu1.pop(0))
print(list_stu1)

list_stu1.insert(0,'xiaoming')
print(list_stu1)

list_stu1.append("zhangsan")
print(list_stu1)


list_person = ['Student','Doctor']

list_new = list_stu1 +list_person
print(list_new)
list_stu1.remove("alice")
print(list_stu1)

new= [item+"test" for item in list_stu1 if item == 'Jack']
print(new)

filter_new = list(filter(lambda item : item == 'Student',list_person))
print(filter_new)


for index,item in enumerate(list_stu1):
    print(f'{index}----{item}')

for item in list_stu1:
    print(f"===={item}")