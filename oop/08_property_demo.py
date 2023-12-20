"""
    python中可以使用property 实现对类属性的get，set操作，实现对属性进行一些计算与校验
"""

class Person:

    def __init__(self,name:str):
        self.__name = name

    @property
    def name(self)->str:
        return f"hello {self.__name}"

    # 此name 需要与定义的property方法名一样，修改属性使用 person.name =value 进行修改
    @name.setter
    def name(self,name):
        if name is None:
            raise  Exception("name cannot be None")
        self.__name = name

    #定义删除属性
    @name.deleter
    def name(self):
        self.__name=None

if __name__ == '__main__':
    person = Person('name')

    print(person.name)

    #修改属性
    # person.name = None
    person.name = 'test'
    print(person.name)
    #删除属性
    del person.name
    print(person.name)