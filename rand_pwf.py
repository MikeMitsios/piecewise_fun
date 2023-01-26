from piecewise_fun import PieceFunction as pf, PiecewiseFunction as pwf
from random import randint, uniform, choice, getrandbits

'''
Create a random PiecewiseFunction object
    param_type: int/float the typr of random function that will be picked
    fun_number: The number of PieceFunctions that PIecewiseFunction will contain
    start: A definition of the domain's start
    max_limit: A limit for randomness
    fun_type: The type of functions that PiecewiseFunction will include. 3 different types (random, constant, linear)

'''
def random_piecewise_funct(param_type:type, fun_number:int, start=0, max_limit=10, fun_type="random"):
    def random_fun_picker(type:type):       #choose the random function based on type
        if type == int:
            rfun = randint
        elif type == float:
            rfun = uniform
        else:
            raise ValueError("Usage: value = int OR value = float.")
        return rfun

    rfun=random_fun_picker(param_type)
    f_type = fun_type
    fun_list = []
    func = ""
    prev_eq = (bool(getrandbits(1)), bool(getrandbits(1)))
    for i in range(fun_number):
        a = rfun(1,max_limit)
        b = rfun(-max_limit,max_limit)
        if fun_type == "random":
            f_type = choice(["constant","linear"])
        if f_type == "constant":
            func=str(a)
        elif f_type == "linear":
            func=str(a) + "*x+" + str(b)
        else:
            raise ValueError("This type of function is supported yet")
        fun_range = rfun(1, max_limit)
        current_eq = (not(prev_eq[1]), bool(getrandbits(1)))
        fun_list.append(pf(start, start + fun_range, current_eq, func))
        prev_eq = current_eq
        start += fun_range

    return pwf(fun_list)