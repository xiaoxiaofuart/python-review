"""
    python中存在__new__方法用于实例化一个对象，这个方法是Object类的，Object类是所有类的父类，实际上一个对象实例化的过程分为两步
    1） 通过 Object.__new__(self,*agrs,**args)生成一个对象
    2）在通过slef.__init__(self,args)进行实例属性的赋值，最终返回一个对象
    __new__一般很少使用，当需要重写父类的实例方法时使用
"""


class Math_Computer(float):
    def __new__(cls, score:float):
        return super().__new__(cls,score*100)



if __name__ == '__main__':
    math_inst = Math_Computer(1.5)

    print(math_inst)#150.0
