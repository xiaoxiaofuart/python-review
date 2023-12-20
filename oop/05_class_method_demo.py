"""
    python中可以使用装饰器@classmethod来定一个方法，将这个方法定义为类方法，类方法可以直接使用
"""


class Animal:
    name = 'test'
    def __init__(self, name: str):
        self.name = name

    @classmethod
    def eat(self,food :str):
        print(f"{self.name} eat the food is {food}")


    #一般用于创建对象
    @classmethod
    def get_instance(self):
        return self




if __name__ == '__main__':
    Animal.eat("rice")

    animal_instance = Animal.get_instance()

    print(animal_instance)