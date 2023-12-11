"""
    1.定义tuple：1）空tuple () 1)定义只有一个元素的tuple 3）定义多个元素的tuple (1,2,3)
    2.tuple可以用加好进行运行，标识两个tuple进行合并 （1,2）+（3,4） => （1,,2,3,4）
"""

tuple1 = ()
tuple12 = (1,)
tuple3 = (1, 2, 3)
tuple3[2, 3]  # (2,)

tuple4 = (1, 2) + (3, 4)

tuple5 = (1, 2) * 3  # (1, 2 ,1, 2 ,1, 2 )

print(1 in tuple3)  # True判断一个元素是否在tuple中
