"""
    python中定义函数用关键字 def
    1.函数形参可以 用 str1；str的形式，表示函数接收一个字符串类型的参数，其中str可写可不写，写的话会让别人更好的读懂函数
    2.函数的返回用return ，方法体上可以用 -> str 表示函数的返回为字符串
    3.函数缺省值：放在参数列表的最后，形式为 str1：str = '我是默认值'
    4.关键字参数：有时候我们可以指定函数参数 = 参数值的形式传参，这样就不用按照参数列表的顺序传参了
    5.lambda表达式：lambda函数相当于一个匿名函数，通过定义入参与出参来进行函数定义，形式为 lambda str1:表达式
"""


def print_str(str1: str):
    print(str1)


def return_str(str1: str) -> str:
    return str1 + " hello"


#   定义一个缺省值函数
def defalut_value_func(str1: str, str2: str = "我是默认值"):
    print(str1 + str2)


def unique_param(name: str, age: int):
    print(f"我的名字{name},年龄是{age}")


func_lambda = lambda str1: print(str1)

func_lambda("cesi")

#   定义一个缺省lambda函数
func1 = lambda str1: str1
print(func1('ceshi1111'))


#   定义一个带lambda函数的函数
def func_param_have_lambda(str1: str, funcs):
    funcs(str1)


func_param_have_lambda("你好呀", lambda str1: print_str(str1))


#   函数的调用
print_str("hello")

print(return_str("python"))

defalut_value_func("ceshi")

unique_param(age=15, name="ceshi")
