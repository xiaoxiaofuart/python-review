
s_num1 = input("请输入第一个数：")
s_num2 = input("请输入第二个数：")

num1 = int(s_num1)
num2 = int(s_num2)

#   交换数字，交换最大值
if num1 > num2:
    num3 = num2
    num2 = num1
    num1 = num3

sum1 = 0
for item in range(num1, num2+1):
    sum1 = sum1 + item

print("最终求和为：" + str(sum1))
