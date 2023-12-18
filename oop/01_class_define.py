
"""
    定义一个类：使用class关键字
"""
class Student:
    pass

class Person:
    pass


def main() ->None:
    #  实例化一个类
    student_inst = Student()
    # 打印类的实例对象
    print(student_inst)
    # 打印类的地址
    print(id(student_inst))
    # 以十六进制的方式打印某个类的地址
    print(hex(id(student_inst)))
    # 判断某个实例是否是某个类的对象
    print(isinstance(student_inst,Student))


if __name__ == '__main__':
    main()