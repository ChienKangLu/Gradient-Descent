import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    y = 1 - (x * math.exp(-x))
    return y


def f_(x):
    return -math.exp(-x) + x * math.exp(-x)


def data():
    X = []
    Y = []
    for x in np.arange(0, 10, 0.01):
        x_value = x
        y_value = round(f(x), 3)
        X.append(x_value)
        Y.append(y_value)
    return X, Y


def draw(X, Y):
    plt.plot(X, Y, color="black", linestyle='-', picker=True)


def onpick(event):
    ind = event.ind
    print('onpick3 scatter:', ind)


def gradient(lr,delta):
    return -lr*delta


def gradient_descent(x,lr, max_iter):
    for iter in range(0, max_iter):
        delta = f_(x)
        x = x + gradient(lr,delta)
        y = f(x)
        print(iter,delta,x,y)
    return x, y


if __name__ == '__main__':
    fig = plt.figure()
    fig.canvas.mpl_connect('pick_event', onpick)

    X, Y = data()
    print(len(X), X)
    print(len(Y), Y)

    draw(X, Y)
    plt.xlabel("x")
    plt.ylabel("y")
    x = 8
    y = f(x)
    plt.scatter(x, y, color="blue", marker='o', linestyle='None', picker=True, s=20*4*2)
    x,y = gradient_descent(8,0.02,30000)
    print("min point",x,y)

    plt.scatter(x, y, color="red", marker='o', linestyle='None', picker=True, s=20*4*2)
    plt.show()
