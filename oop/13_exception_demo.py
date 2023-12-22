"""
    python中异常与java类型，顶层的异常为BaseException，底下为 SystemException、KeyIntereptException、Exception
    而我们日常开发中都是基于Exception 进行编程，使用 try ... except  异常类型进行捕获
    使用 raise Exception('异常信息') 进行异常的手动抛出
"""


class MyExceptin(Exception):
    def __init__(self, *args):
        super().__init__(self, *args)



def add(num1,num2):
    if not isinstance(num1,int) or not isinstance(num2,int):
        raise MyExceptin('Argument is not invalid')
    print(str(num1+num2))



if __name__ == '__main__':
    try:
        add('1', '2')
    except MyExceptin as myexpcet:
        print(f'报错啦{myexpcet}')
