def flatten(x):
    for i in range(len(x)):
        if isinstance(x[i], list):
            x[i] = "'{flatten}'".format(flatten=flatten(x[i]))
    return ' '.join(x)
