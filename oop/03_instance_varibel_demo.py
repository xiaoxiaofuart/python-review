


class Student:
    #定义一个实例方法，第一个参数必须为self
    def read_book(self,book_name:str):
        print(f"I'm reading th book {book_name}")

    #python中__init__方法是一个初始化方法，类似与java中的构造函数，在实例化类的时候调用
    def __init__(self,name:str):
        self.name = name





if __name__ == '__main__':
    isinstance_stu = Student('Tom')
    #方法的调用
    isinstance_stu.read_book("one day")

    #定义实例的变量有两种方法，一种就是上面收到的__init__函数中定义，第二个就是通过实例对象.attr直接定义，只对当前实例有效

    isinstance_stu.male = '男'

    print(isinstance_stu.male)
