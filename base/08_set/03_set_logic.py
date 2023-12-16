"""
    python中支持集合的各个差集计算
    1）集合A中不包含与集合B中相交的部分
    2）集合A与集合B中不包含相交的部分
"""


set_a = {1, 2, 3}

set_b = {2, 3, 4}

# 集合A中不包含与集合B中相交的部分
print(set_a - set_b)
print(set_a.difference(set_b))


#   集合A与集合B中不包含相交的部分
print(set_a.symmetric_difference(set_b))


