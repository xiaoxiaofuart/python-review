"""
    python中也支持定义类的是有属性与方法，通过在方法或者属性前面加一个下划线进行定义，定义一个是有属性仍然能够被使用，
    python没有做强制限制，通过前面加下划线类名称进行调用，类的内部可以使用私有属性与方法
    _filed 表示被保护的，使用实例.属性仍然可以使用
    __field 表示私有的，直接使用会报错，可以通过 _类名称__field进行访问
"""

class Student:
    def __init__(self,name:str,age:str):
        self._name = name
        self._age = age
        self.__private_name = name

    def _print_stu_info(self)->None:
        #类的内部可以使用私有属性
        print(f"student name is {self._name} ,age is {self._age}")



    def __priv_func(self):
        print(self.__private_name)




if __name__ == '__main__':
    inst_stu = Student('jack','21')
    # 强制使用也可以调用
    inst_stu._print_stu_info()
    print(inst_stu._name)

    #属性带两个下划线不能直接使用，会报错
    #print(inst_stu.__private_name)

    # 通过 _类的名称__属性可以访问
    print(inst_stu._Student__private_name)

    # 类是有方法也是一样
    #inst_stu.__priv_func()
    inst_stu._Student__priv_func()