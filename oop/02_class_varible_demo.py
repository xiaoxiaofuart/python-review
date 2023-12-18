from pprint import pprint


class Student:
    # 定义一个类变量
    name = 'student'


def main() ->None:
    # 读取类变量，变量不存在会报错
    print(Student.name)
    # 打印类的名称
    print(Student.__name__)
    # 通过getattr方法获取一个类变量，不存在也会报错
    print(getattr(Student, 'name'))
    # 通过getattr方法获取一个类变量，不存在会返回NaN
    print(getattr(Student,'test','NaN'))

    # 修改类变量的值
    setattr(Student,'name','test')
    print(Student.name)

    # 可以添加一个不存在的变量
    setattr(Student, 'test', 'test1')
    print(Student.test)

if __name__ == '__main__':
    main()
    # python中类变量是存在__dict__中的，是一个字典结构
    pprint(Student.__dict__)