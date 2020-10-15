# !/usr/bin/python3


def bin_search(a_list, s):
    if s < a_list[0] or s > a_list[-1]:
        return False
    right = len(a_list) - 1
    left = 0
    while left <= right:
        mid = (left + right) // 2
        if a_list[mid] > s:
            right = mid - 1
        elif a_list[mid] < s:
            left = mid + 1
        else:
            return s
    return False



class NunIter:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


def fn(n):
    if n < 3:
        return n
    return fn(n-1) + fn(n-2)

print(fn(5))

import sys


def fibonacci(n):  # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()
