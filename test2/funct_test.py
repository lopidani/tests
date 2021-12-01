# Construct a function which has as argument a number and which print the
# result of multiplying nr digits until the last multiply has only one digit
# Ex: functie(999) ==> 9x9x9=729 ==> 7x2x9 ==> 126 ==> 1x2x6=12 ==> 1x2 ==>
# rezultat final 2

# variable for result of multiply
result = int()


def functie(nr):
    # variable for multiply items inside a string
    p = 1
    s = int()
    # make variable result functional inside function
    global result
    for i in range(len(str(nr))):
        p = p * int(str(nr)[i])
        # iteration is at the end
        if i == len(str(nr)) - 1:
            # if multiply has more than 2 caracters we must use ciclic
            # the same function so we introduce s variable
            if len(str(p)) > 2:
                # use the same function for new number p
                s = p
                # if p has 2 digits we must check result of
                # multiplying those digits
            if len(str(p)) == 2:
                # if result of multiplying those digits has
                # 2 digits or more we must continue with multiply
                # until result will have one digit
                if len(str(int(str(p)[0]) * int(str(p)[1]))) > 1:
                    continue
                else:
                    result = int(str(p)[0]) * int(str(p)[1])
                    break
            if len(str(p)) == 1:
                result = p
                break

    if s != 0:
        functie(s)
    return result


print(functie(999))
