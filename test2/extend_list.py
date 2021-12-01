# Punctul1
# Se da functia extendlist si urmatoarele liste l1,l2,l3
# generate de functia extendlist.Cat sunt l1,l2 si l3 ?


def extendlist(val, list=[]):
    list.append(val)
    return list


l1 = extendlist(3)
l2 = extendlist(6, [])
l3 = extendlist("a")
# Raspuns :
l1 = [3, "a"]
l2 = [6]
l3 = [3, "a"]


# Punctul2
# Cat sunt acum l1,l2 si l3 ?
def extendlist(val, list=None):
    if list is None:
        list = []
    list.append(val)


l1 = extendlist(3)
l2 = extendlist(6, [])
l3 = extendlist("a")


# Raspuns :
l1 = [3]
l2 = [6]
l3 = ["a"]
