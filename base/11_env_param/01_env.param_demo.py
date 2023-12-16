"""
    python 中支持获取运行时传递的函数，第一个参数是python的文件名，第二个参数以及后面的参数表示运行程序时传递的参数
"""
import sys


def mian():
    for arg in sys.argv:
        print(arg)


if __name__ == "__main__":
    mian()