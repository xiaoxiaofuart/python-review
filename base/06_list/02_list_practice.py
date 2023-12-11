"""
    练习一个list程序要求实现
    1.获取录入的分数，将其放入一个list中
    2.求分数的平均值
    3.输出大于平均分的数
"""


def get_list_score(score: str) -> list:
    return input_str.split(",")


def get_score_avg(list_score: list) -> float:
    sum_score = 0

    for item in list_score:
        sum_score = sum_score + float(item)

    return sum_score / len(list_score)


def get_above_avg_score(list_score: list, avg: float) -> list:
    output_score_list = []
    for item in list_score:
        if float(item) > avg:
            output_score_list.append(item)
    return output_score_list


input_str = input("请输入分数，以逗号分隔：")
input_list = get_list_score(input_str)
avg = get_score_avg(input_list)
above_avg_list = get_above_avg_score(input_list, avg)
print(f"高于平均数为{above_avg_list}")
