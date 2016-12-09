

ls  = [3, 12, 35, 19, 5]

def max_element(ls):
    max = 0
    for i in ls:
        if i > max:
            max = i
    return max

print("max element: {0}".format(max_element(ls)))
