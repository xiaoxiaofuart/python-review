import csv
import os
import pathlib
"""
    python 中写入csv有两种方式，一种直接按行写入，一种按照定义文件头的形式写入
    1.直接写入
        1）首先打开文件
        2）通过csv.write(file_instance)获得csv文件
        3）写入csv文件两种方式，1.直接写入一行2.直接写入多行
    2.通过dictwrite写入
        1）首先打开文件
        2）通过csv.DictWrite获得文件，需传入两个参数，第一个是文件实例，第二个是文件头
        3）将list[dict]数据写入文件
        4）关闭文件流
"""

def write_list_csv() ->None:
    path_exists = os.path.exists("student.csv")
    file_instance = None
    if not path_exists:
        file_instance = open("student.csv", "x",encoding="utf-8")
    else:
        file_instance = open("student.csv", encoding="utf-8")


    file_csv = csv.writer(file_instance)
    # 要用引号标识一个整体不然会按照每个字符去写
    file_csv.writerow(["lisa",78,89,90])

    file_csv.writerows([["xiaoming,80,86,89"],["xiaohong,56,55,43"],["xiaolei,79,75,71"]])

    file_instance.close()


def write_dict_csv(file_name:str) -> None:
    file_exists = pathlib.Path(file_name).exists()
    file_instance = None
    if not file_exists:
        file_instance = open(file_name, "w", encoding="utf-8")
    else:
        file_instance = open(file_name,"a",encoding="utf-8")

    csv_dict = csv.DictWriter(file_instance,fieldnames=["name","age","sex"])

    csv_dict.writeheader()

    dict_stu = [
        {
            'name':'zhangsan',
            'age': 15,
            'sex': 'male',
        },
        {
            'name': 'lisi',
            'age': 18,
            'sex': 'male',
        },
        {
            'name': 'wangwu',
            'age': 29,
            'sex': 'female',
        }
    ]

    csv_dict.writerows(dict_stu)

    file_instance.close()


if __name__ == "__main__":
    write_dict_csv("mytest.csv")


