"""
    python中异常的格式为 try: except： else: finally:
    其中try块中表示需要捕获的异常代码块
    except表示要捕获的异常，支撑写多个异常
    else为不是异常时执行的代码
    finally 是不论异常还是正常，均要执行的代码
"""

try:
    i = 10/'s'
    print("正常执行完毕")
except ZeroDivisionError as e:
    print("算数异常啦！")
except:
    print("我执行异常啦！")
else:
    print("正常逻辑执行完毕后执行")
finally:
    print("不论成功还是失败，我都会执行")
