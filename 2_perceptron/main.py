# OR
# (w1, w2, θ) = (0.5, 0, 0.3)
# (x1, x2) = (0, 0) , 0.0 + 0.0 < 0.3
# (x1, x2) = (1, 0) , 0.5 + 0.0 > 0.3
# (x1, x2) = (0, 1) , 0.0 + 0.5 > 0.3
# (x1, x2) = (1, 1) , 0.5 + 0.5 > 0.3

# AND
def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1*w2 + x2*w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1
    else:
        # never execute
        pass


def main():
    print(AND(0, 0))
    print(AND(1, 0))
    print(AND(0, 1))
    print(AND(1, 1))


if __name__ == '__main__':
    main()
