"""
    python中枚举的定义 需要集成Enum 类，
    1）获取枚举的名称 Interface_Status.SUCCESS.name
    2）获取枚举的值 Interface_Status.SUCCESS.value
    3) 枚举的遍历： for staus in Interface_Status: 得到的是一个枚举实例，获取name方式staus.name
"""

from enum import Enum


class Interface_Status(Enum):
    SUCCESS = 1
    fail = 2




if __name__ == '__main__':

    # 获取枚举的名称
    print(f"sucess code is {Interface_Status.SUCCESS.name}")
    #获取枚举的值
    print(f"sucess code is {Interface_Status.SUCCESS.value}")

    # 遍历枚举,得到的是一个枚举的对象
    for staus in Interface_Status:
        print(f"Enum name is {staus.name},value is {staus.value}")

    # 值比较
    print(Interface_Status.SUCCESS.value is 1) #True

    # 根据name 获取 枚举对象
    print(Interface_Status['SUCCESS']) #Interface_Status.SUCCESS

    #根据value获取枚举对象

    print(Interface_Status(1)) #Interface_Status.SUCCESS

