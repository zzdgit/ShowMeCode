# # coding=utf-8
# import sys
# import pandas as pd
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     data = []
#     for i in range(n):
#         line = sys.stdin.readline().strip()
#         data.append(line.split())
#     df = pd.DataFrame(data)
#     lie = df.apply(lambda x: x.sum(), axis=1)
#     hang = df.apply(lambda x: x.sum)
#     a_lie = list(set(lie))
#     a_sum = 0
#     if lie.count(a_lie[0]) == 1:
#         i = lie.index(a_lie[0])
#         a_sum = a_lie[1]
#     else:
#         i = lie.index(a_lie[1])
#         a_sum = a_lie[0]
#     a_hang = list(set(hang))
#     if hang.count(a_hang[0]) == 1:
#         j = hang.index(a_hang[0])
#     else:
#         j = hang.index(a_hang[1])
#     one_h = df.loc[j-1:0].to_list()
#     num = a_sum - sum(one_h.pop(i-1))
#     print(j, i, num)



import sys
if __name__ == "__main__":
    data = []
    # for i in range(2):
    #     line = sys.stdin.readline().strip()
    #     data.append(line)
    # a = data[0]
    # b = data[1]
    a = 'bbb'
    b = 'bb'
    a = a.replace(' ', '')
    a = a.replace('\t', '')
    l = len(b)
    count = 0
    for i in range(len(a)-len(b)+1):
        if b == a[i:i+l]:
            count = count + 1
    print(count)













#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    data = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = line.split(',')
        data.append(values)
    m = int(sys.stdin.readline().strip())
    flag = False
    for j in range(m):
        line = sys.stdin.readline().strip()
        values = [int(i) for i in line.split(',')]
        for k in range(max(values[0], values[1])):
            if values[0] - k >= 0:
                data[values[0] - k][values[1]] == 0
            else:
                print(j)
                flag = True
                break
            if values[1] - k >= 0:
                data[values[1] - k][values[3]] == 0
            else:
                print(j)
                flag = True
                break
        if flag:
            break
    print('ok')
    print('ok')

\










# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    data = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = line.split(',')
        data.append(values)
    m = int(sys.stdin.readline().strip())
    flag = False
    for j in range(m):
        line = sys.stdin.readline().strip()
        values = [int(i) for i in line.split(',')]
        for k in range(max(values[0], values[1])):
            if values[0] - k >= 0:
                data[values[0] - k - 1][values[1]] == 0
            else:
                print(j)
                flag = True
                break
            if values[1] - k - 1 >= 0:
                data[values[1] - k - 1][values[3]] == 0
            else:
                print(j)
                flag = True
                break
        if flag:
            break
        break
    print('ok')

# coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys

if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())
    data = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = line.split(',')
        data.append(values)
    m = int(sys.stdin.readline().strip())
    flag = False
    for j in range(m):
        line = sys.stdin.readline().strip()
        values = [int(i) for i in line.split(',')]
        for k in range(max(values[0], values[1])):
            if values[0] - k >= 0:
                if data[values[0] - k][values[1]] != 0:
                    print(j)
                    flag = True
                    break
            if values[1] - k >= 0:
                if data[values[1] - k][values[3]] != 0:
                    print(j)
                    flag = True
                    break
        if not flag:
            break
    if not flag:
        print('ok')





