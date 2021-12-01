# how use variable from a function in other function
# varianta1
def func1():
    func1.var = "func1 var"


def func2():
    func1()
    print(func1.var)


# varianta2
def func1():
    var = "funct1 var"
    return var


def func2():
    print(func1())


# varianta3
def func1():
    global var
    var = "funct1 var"


def func2():
    func1()
    print(var)


if __name__ == "__main__":
    # varianta1
    func2()
    # varianta2
    func2()
    # varianta3
    func2()
