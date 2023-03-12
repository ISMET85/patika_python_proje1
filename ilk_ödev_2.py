


def reserve_list(n):
    n=n[::-1]
    n = [i[::-1] for i in n]
    return n

liste1=[[1, 2], [3, 4], [5, 6, 7]]


print(reserve_list(liste1))