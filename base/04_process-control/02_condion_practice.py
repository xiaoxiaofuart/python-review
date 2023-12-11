"""
    用户输入一个分数，判断
    分数小于60 不合格
    分数大于等于60 小于70 合格
    分数大于等于70 小于80 一般
    分数大于等于80小于90 良好
    分数大于等于90，小于等于100 优秀
    其他输出成绩不合法
"""

input1 = input("please input a score:")

score = float(input1)

if 90 <= score <= 100:
    print("It's very good!")
elif 80 <= score < 90:
    print("It's good")
elif 70 <= score <= 80:
    print("It's ok")
elif 60 <= score < 70:
    print("It's not good")
elif 0 <= score < 60:
    print("It's terrable")
else:
    print("The score is not correct")


