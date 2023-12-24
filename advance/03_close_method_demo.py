"""
    python 中存在闭包函数，也就是函数内部的变量别函数内部的函数进行引用，同时此函数返回的是这个函数的内部函数，那么python
    中将此称作闭包，实现的底层原理是内部python 对于内部函数引用外部函数的变量，会将这个变量拷贝到内部函数的__couser__方法
    中进行保存
"""


def out_method():
    str1 = "hi"

    # 内部函数引用外部变量str1
    def inner_method():
        print(f"This is {str1}")

    str1 = "hello python"

    # 返回内部函数
    return inner_method()


if __name__ == '__main__':
    out_method()  # This is hello python
