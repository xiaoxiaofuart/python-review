"""
    python 中支持一个类继承多个父类，可以实现其中方法，但是当父类中有重复的方法名时，，按照继承的顺序，先继承的方法为有效
    如果想指定父类的方法作为实现，可以将直接指定父类的方法
"""


class Person:
    def run(self, speed: str):
        print("Person is running")


    def sleep(self):
        print("Person need Sleep")


class Animal:
    def run(self, speed: str):
        print("Animal is running")

    def sleep(self):
        print("Animal need sleep")


class Student(Animal, Person):
    def sleep(self):
        #直接指定父类方法调用
        Person.sleep(self)


if __name__ == '__main__':
    stu_inst = Student()
    # Animal继承在先，所以执行的是Animal 的 run方法
    stu_inst.run("test")  # Animal is running
    stu_inst.sleep()
