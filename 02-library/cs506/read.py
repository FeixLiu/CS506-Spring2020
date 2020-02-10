def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    # raise NotImplementedError()
    file = open(csv_file_path, 'r')
    rst = []
    for line in file:
        line = line.replace('\n', '')
        line = line.split(',')
        temp = []
        for a in line:
            temp.append(eval(a))
        rst.append(temp)
    return rst
