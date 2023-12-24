"""
    python中多线程的定义有多种方式
    1)直接使用thread 类的api完成多线程定义，运行
    2）继承thread类，实现run方法
    3）使用线程池Thraadepoolexcutor提交多线程
"""
import time
from concurrent.futures import ThreadPoolExecutor
from threading import Thread


def print_nums(str1: str):
    for i in range(10):
        print(f"{str1}-{i}")
        time.sleep(0.01)


if __name__ == '__main__':
    # thread_inst1 = Thread(target=print_nums("my_task" + str(1)))  # ,args=用于执行线程传递参数
    # thread_inst1.setName("my_task" + str(1))
    # thread_inst2 = Thread(target=print_nums("my_task" + str(2)))
    # thread_inst2.setName("my_task" + str(2))
    # thread_inst3 = Thread(target=print_nums("my_task" + str(3)))
    # thread_inst3.setName("my_task" + str(3))
    #
    # thread_inst1.start()
    # thread_inst2.start()
    # thread_inst3.start()

    # join 方法会让外层的线程等待线程执行完成在执行
    # thread_inst1.join()

    # 线程池执行多线程
    with ThreadPoolExecutor() as  executors:
       thead_inst1 = executors.submit(print_nums("线程A"))
       thead_inst2 = executors.submit(print_nums("线程B"))

class PrintThread(Thread):
    def __init__(self):
        print("I‘m initing")

    def run(self) -> None:
        for i in range(10):
            print(f"{self.name}-{i}")
