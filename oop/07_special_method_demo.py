"""
    python中包含一些特殊方法，在特殊的场景下会触发调用，用户可预先定义好此方法
    1）__str__ 用于打印对象，当调用str（）函数时触发调用
    2）__repr__ 用于给机器添加对象的标识
    3）__eq__ 在进行两个对象比较，即 == 的时候进行调用
    4）__hash__ 定义对象的hash值，在使用hash()函数时进行调用
    5）__del__ 当一个对象被垃圾回收的时候会进行调用
    6)__bool__
    7）__len__
"""


class Person:
    def __init__(self, name: str, age: int, addr: str):
        self.name = name
        self.age = age
        self.addr = addr

    def get_instance(self, name: str, age: int, addr: str):
        return self(name, age, addr)

    # 调用str函数时会被调用
    def __str__(self):
        return "my name is " + self.name + ",I'm " + str(self.age) + " years old ,and I'm from " + self.addr

    # 在进行对象比较的时候调用
    def __eq__(self, other) -> bool:
        if not isinstance(other, Person):
            return False;
        return self.name == other.name and self.age == other.age and self.addr == other.addr

    # 在使用hash的使用调用
    def __hash__(self):
        return hash(self.name)

    # 当对象被bool函数解析的时候调用，若类中未定义bool函数，将寻找len函数进行解析
    def __bool__(self) -> bool:
        return not self == None

    def __len__(self) -> bool:
        return not self == None

    # 对象被回收的时候调用
    def __del__(self):
        print("I'm called when garbage start")


if __name__ == "__main__":
    per_instance1 = Person.get_instance(Person, "小明", 15, '安徽')
    per_instance2 = Person.get_instance(Person, "小明", 15, '安徽')
    per_instance3 = Person.get_instance(Person, "小宏", 15, '安徽')
    per_instance4 = per_instance2

    # is 函数用于判断两个对象是否指向同一个实例
    print(per_instance3 is per_instance2)  # False
    print(per_instance4 is per_instance2)  # True
    # 调用eq方法进行比较
    print(per_instance1 == per_instance2)
    # 调用str函数
    print(per_instance1)
    # 调用类中的bool方法，若没有会调用len方法
    print(bool(per_instance1))
    # 调用hash方法
    print(hash(per_instance1))
