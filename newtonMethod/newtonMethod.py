from numpy import *

# 存系数的矩阵
coefficient_list = []


# 算出当前x的函数值
def f(x):
    fx = 0
    for i in range(0, len(coefficient_list)):
        fx = fx + coefficient_list[i] * (x ** i)
    return fx


# 算出当前x的导函数值
def fd(x):
    fdx = 0
    for i in range(1, len(coefficient_list)):
        fdx = fdx + coefficient_list[i] * i * (x ** (i - 1))
    return fdx


def newtonMethod(time, now_x):
    x = now_x
    a = f(x)
    b = fd(x)
    print('fx = ' + str(a) + ',fdx = ' + str(b) + 'newtonMethodTime = ' + str(time))
    if f(x) == 0.0:
        return time, x
    else:
        next = x - a / b
        print('next x = ' + str(next))
    if a - f(next) < 1e-6:
        print('meet f(x) = 0 , x = ' + str(next))  # 误差小于1e-6 跳出迭代，输出fx
    else:
        return newtonMethod(time + 1, next)


if __name__ == "__main__":
    # 输入一个表达式的系数，从低此开始输入，回车键分隔
    # 如想输入 f(x) = 5 + 4*x + 3*x^2
    # 5 <-回车
    # 4 <-回车
    # 3 <-回车
    # x <-回车
    while True:
        x = input()
        if x == 'x':
            break
        else:
            coefficient_list.append(float(x))
    # 第一个参数代表迭代次数 第二个参数代表从x = ? 开始迭代
    newtonMethod(0, 4.0)
