
"""
    python中使用@staticmethod 定义一个静态方法，主要用来做一些工具类，用于直接调用
"""

class Strutil:

    @staticmethod
    def print_name(name: str):
        print(f"I'm name: {name}")




if __name__ == '__main__':
    Strutil.print_name("xiaoming")