"""
    python 中存着资源管理器用于管理上下文处理，基本语法如下
    with 函数或者方法 as object:
        代码块
    这样就能直接通过方法调用，不用关系，其他特殊的操作，比如open 函数获取一个文件流，通过上下文管理处理的时候就不需要关心文件流的关闭
    python 会自动处理这些流的关闭

    自定义一个上下文管理器需要实现__enter__ 和 __exit__方法 当whit 类的时候会调用enter方法返回的实例，当方法体结束的时候会调用
    exit 方法自动退出
"""
import time


# 定义一个上下文管理器需要实现__enter__与 __exit__ 方法
class My_Context_Manager:
    def __init__(self):
        self.time_escape = 0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.time_escape = time.perf_counter() - self.start_time
        print(f"The process cost {self.time_escape} second")


if __name__ == '__main__':
    # 通过with 函数返回一个上下文管理对象，可以对实例进行上下文处理，不用关心一些资源释放等处理
    with open("1.txt", "w") as file_instance:
        file_instance.write("hello python")

    print("mian is end")

    with My_Context_Manager() as instance_context:
        for i in range(10):
            time.sleep(1)
