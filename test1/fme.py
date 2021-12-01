# global variable result of multiply
result = int()


def fme(nr):
    # variable p for initialize multiply of nr digits
    p = 1
    # variable s for reuse functions fme argument
    s = int()
    global result
    for i in range(len(str(nr))):
        p = p*int(str(nr)[i])
        # when iteration is at the last digit
        if i == len(str(nr))-1:
            # if product of multiplication len is more than two digits (we must
            # use ciclic the same function fme)
            if len(str(p)) >= 2:
                # than we must reuse the function
                s = p
            # if p has 2 digits we must check the result of multiplication
            # of those digits
            if len(str(p)) == 2:
                # if the result of multipication of those digits has 2 digits
                # or more we must continue with multiply
                # until result should have one digit
                if len(str(int(str(p)[0])*int(str(p)[1]))) > 1:
                    continue
                else:
                    result = int(str(p)[0])*int(str(p)[1])
                    break
            if len(str(p)) == 1:
                result = p
                break

    if s != 0:
        fme(s)
    return result


if __name__ == "__main__":
    nr = 292
    print('fme=', fme(nr))
