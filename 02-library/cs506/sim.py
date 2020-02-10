def euclidean_dist(x, y):
    # raise NotImplementedError()
    rst = 0
    for i in range(len(x)):
        rst = rst + (x[i] - y[i]) * (x[i] - y[i])
    return pow(rst, 0.5)


def manhattan_dist(x, y):
    # raise NotImplementedError()
    rst = 0
    for i in range(len(x)):
        if x[i] != y[1]:
            rst += 1
    return rst


def jaccard_dist(x, y):
    # raise NotImplementedError()
    set_x = set(x)
    set_y = set(y)
    return 1 - len(set_x & set_y) / len(set_x | set_y)


def cosine_sim(x, y):
    # raise NotImplementedError()
    sum_x = 0
    sum_y = 0
    sum_all = 0
    for i in range(len(x)):
        sum_x += x[i] * x[i]
        sum_y += y[i] * y[i]
        sum_all += x[i] * y[i]
    return sum_all / (pow(sum_x, 0.5) * pow(sum_y, 0.5))

# Feel free to add more
