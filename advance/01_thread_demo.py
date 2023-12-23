"""
    python 中可以继承Thread类方式 创建一个线程,重写init方法 实现start方法
"""
from threading import Thread


class My_Thread(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.setName(name)

    def run(self) -> None:
        for num in range(100):
            print(f"{self.name}--{num}")


if __name__ == '__main__':
    thread_ins1 = My_Thread("thread1")
    thread_ins2 = My_Thread("thread2")
    thread_ins3 = My_Thread("thread3")

    thread_ins1.start()
    thread_ins2.start()
    thread_ins3.start()