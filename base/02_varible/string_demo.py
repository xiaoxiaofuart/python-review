# 定义字符串 python
name = "my name is \" david\""

# python 中有 r 表示原生的意思，这样就不会对特殊字符进行转义
test = r"this is \ python \ "

# python 中可以使用f 表示对字符串进行格式化，用于替换变量
student_name = "xiaoming"
student_desc = f"stundene name {student_name}"
print("学生描述为："+student_desc)


# 定义一个字符串的获取第一个字符
str = "hello"
print("第一个字符为："+str[0])
print("字符的长度为："+len(str).__str__()) # 获取字符串的长度
print("截取字符串："+str[1:3]) # 截取1到3的字符串吗不包含3
print("截取字符串："+str[1:]) # 截取字符串到末尾

