

ls  = [3, 12, -35, 11, 7]

def linear_search(ls, x):
    for i in ls:
        if i == x:
            return i
    return None

print(linear_search(ls, 11))
