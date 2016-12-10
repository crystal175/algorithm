

ls  = [3, 12, -35, 11, 7]

def sum_elemetns(ls):
    sum = 0
    for i in ls:
        sum = sum + i
    return sum

print("sum elements: {0}".format(sum_elemetns(ls)))
