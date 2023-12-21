"""
    python 中方法的重写与java类似，如果需要调用父类的方法，可以使用super().method进行调用
"""



class Person:
    def __init__(self):
        print("Person  is start init ")

    def eat(self,food:str):
        print(f"eat something like {food}")



class Student(Person):
    def __init__(self):
        print("Son  is start init ")

    def eat(self, food: str):
        #super().eat(food)
        print(f"son eat something like {food}")




if __name__ == "__main__":

    #父类的引用指向子类的对象
    person:Person = Student()

    person.eat("food")#son eat something like food