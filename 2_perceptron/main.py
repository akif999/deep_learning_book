# OR
# (w1, w2, θ) = (0.5, 0, 0.3)
# (x1, x2) = (0, 0) , 0.0 + 0.0 < 0.3
# (x1, x2) = (1, 0) , 0.5 + 0.0 > 0.3
# (x1, x2) = (0, 1) , 0.0 + 0.5 > 0.3
# (x1, x2) = (1, 1) , 0.5 + 0.5 > 0.3
import numpy as np


# AND
def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# NAND
def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


# OR
def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = np.sum(w*x) + b
    if tmp <= 0:
        return 0
    else:
        return 1


def main():
    print('AND')
    print(AND(0, 0))
    print(AND(1, 0))
    print(AND(0, 1))
    print(AND(1, 1))
    print('NAND')
    print(NAND(0, 0))
    print(NAND(1, 0))
    print(NAND(0, 1))
    print(NAND(1, 1))
    print('OR')
    print(OR(0, 0))
    print(OR(1, 0))
    print(OR(0, 1))
    print(OR(1, 1))


if __name__ == '__main__':
    main()
