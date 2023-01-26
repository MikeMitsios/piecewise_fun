from exceptions import WrongType, RangeError, FunctionFormat, RangeInconsistency, OutOfRange, ListIndexOutOFRange, FloatIndex
import numpy as np
from matplotlib import pyplot as plt
from itertools import cycle
from utils import binary_search, math_function_regex, colorstring


class PieceFunction:
    """A structure to define a function object
    A PieceFunction consists of:
    Attributes:
        start: The x where the function starts
        end: The x where the function ends
        function: The format of the function (string)
        equal: A boolean tuple that shows whether the start and end of the field are included
    Functions:
        __input_verification: This functions check if the given arguments have the right type.
        eval: The evaluation of x for the given a function.
        plot: Returns the chart of the function.
        get_min: Finds the minimum value of the function. Because we have only constant and linear function we check only the edges of the domain.
        get_max: Finds the maximum value of the function.
        __str__: The string form of the function.
        report_f: Returns a small report of the Piecefunction
    """
    def __init__(self, start:float, end:float, equal:tuple, function:str):
        self.__input_verification(start, end, equal, function)
        self.start: float = start
        self.end: float = end
        self.function: str = function
        self.equal: tuple = equal

    def __input_verification(self, start:float, end:float, equal:tuple, function:str):
        if not isinstance(start, (int,float)): raise WrongType("start", type(start), "int/float")
        if not isinstance(end, (int,float)): raise WrongType("end", type(end), "int/float")
        if not start<end: raise RangeError(start, end)
        if not (isinstance(equal, tuple) and len(equal)==2 and isinstance(equal[0], bool) and isinstance(equal[1], bool)):
            raise WrongType("equal", type(equal), "tuple(bool, bool)")
        if not isinstance(function, str): raise WrongType("function", type(end), "str")
        if not math_function_regex.match(function): raise FunctionFormat(function)

    def eval(self, x:float, plot_mode:bool=False) -> float:
        if plot_mode: return eval(self.function, {"x": x})
        if (x == self.end and self.equal[1]) or (x < self.end and x > self.start) or (x == self.start and self.equal[0]): #(x < self.end and x > self.start) or
            return eval(self.function, {"x": x})
        else:
            raise OutOfRange(x, self.function)        

    def plot(self, show:bool=True, f_color='red'):
        def points_plot(eq, pos):    
            fill_style = 'full' if eq else 'none'                          
            plt.plot(x[pos], y[pos], fillstyle=fill_style, marker='o', color=f_color)    
        x = np.linspace(self.start, self.end, 2)  # 2 points need to represent constant and linear funcs
        y = np.full(x.shape, self.eval(x, True))
        plt.plot(x, y, color=f_color)
        points_plot(self.equal[0],0)    # Checks if the start edges is included to the domain
        points_plot(self.equal[1],-1)   # Checks if the end edges is included to the domain
        if show: plt.show()

    def get_min(self) -> float:
        return min(self.eval(self.start, True), self.eval(self.end, True))
    
    def get_max(self) -> float:
        return max(self.eval(self.start, True), self.eval(self.end, True))

    def __str__(self) -> str:
        p_start = "[" if self.equal[0] else "("
        p_end = "]" if self.equal[1] else ")"
        return "f(x)=" + self.function + ", x in "+p_start + str(self.start) + "," + str(self.end) + p_end

    def report_f(self):
        print(self)
        self.plot()


class PiecewiseFunction:
    """A class that store and manages many PieceFunction objects
        A PiecewiseFunction object contains a list with many PieceFunctions. Each one of the PieceFunctions' domains must not overlap one the other.

        Attributes:
            The main attribute in this class is self.__function_list (private). This is the list that contains many PieceFunctions
        Functions:
            __input_verification: A type check for the given arguments.
            __ranges_inconsistency: This function checks whether the given functions and their domains do not have any range inconsistency (one domain overlaps another).
            __len__: The size of the list of PieceFunctions.
            eval: A function that uses a binary search to locate the function that calculates the value of x. Then finds this value.
            add_fun: This method add a function to the list. The function's domain MUST NOT overlap a domain of an already existed function.
            remove_fun: Removes a function given a specific index.
            get_fun: Given an index returns the object of the function.
            plot_fun: Given an index plot the functions in this position
            get_min: Calculate the global min comparing all the mins of the PieceFunctions. Each time has to be calculated because the PiecewiseFunction may be modified (add/remove fun)
            get_max: Calculate the global max comparing all the maxs of the PieceFunctions. Each time has to be calculated because the PiecewiseFunction may be modified (add/remove fun)
            __str__: The string form of the function.
            report_f: Returns a small report of the Piecewisefunction
            plot: Returns the chart of the function.
    """
    def __init__(self, function_list:list):
        self.__input_verification(function_list)
        self.__function_list = sorted(function_list, key=lambda x: x.start)
        self.__ranges_inconsistency()

    def __input_verification(self, function_list:list):
        if not isinstance(function_list, list): raise WrongType("function_list", type(function_list), "list")
        for i, f in enumerate(function_list):
            if not isinstance(f, PieceFunction):
                raise WrongType("Item " + str(i) + " in function_list", type(f), "PieceFunction")

    def __ranges_inconsistency(self):
        for i in range(len(self.__function_list)-1):
            if self.__function_list[i].end > self.__function_list[i+1].start:
                raise RangeInconsistency(i,str(self.__function_list[i]), i+1, str(self.__function_list[i+1]) )
            if self.__function_list[i].end == self.__function_list[i+1].start and self.__function_list[i].equal[1] and self.__function_list[i+1].equal[0]:
                raise RangeInconsistency(i,str(self.__function_list[i]), i+1, str(self.__function_list[i+1]) )

    def __len__(self) -> int:
        return len(self.__function_list)

    def eval(self, x:float) -> float:
        f_index=binary_search(self.__function_list, x)
        if f_index == -1:
            raise OutOfRange(x, self.__function_list)
        else:
            return self.__function_list[f_index].eval(x)

    def add_fun(self, fun:PieceFunction):
        if not isinstance(fun, PieceFunction):
            raise WrongType("Added item in function_list", type(fun), "PieceFunction")
        pos = len(self.__function_list)
        for i,f in enumerate(self.__function_list):
            if f.start > fun.end or (f.start == fun.end and f.equal[0] != fun.equal[1]):
                pos=i
                break
            if f.start < fun.start:
                break      
        if pos == 0:
            self.__function_list.insert(pos,fun)
        else:
            if self.__function_list[pos-1].end < fun.start or (self.__function_list[pos-1].end == fun.start and 
            self.__function_list[pos-1].equal[1] != fun.equal[0] ):
                self.__function_list.insert(pos,fun)
            else:
                raise ValueError(str(fun) + " cannot be added due to range intersection with other functions")
        return pos

    def remove_fun(self, index:int):
        if type(index) != int: raise FloatIndex(index)
        fl_len=len(self.__function_list)
        if index>=fl_len: raise ListIndexOutOFRange(index,fl_len)
        del self.__function_list[index]

    def get_fun(self, index:int) -> PieceFunction:
        if type(index) != int: raise FloatIndex(index)
        fl_len=len(self.__function_list)
        if index>=fl_len: raise ListIndexOutOFRange(index,fl_len)
        return self.__function_list[index]

    def plot_fun(self, index:int):
        if type(index) != int: raise FloatIndex(index)
        fl_len=len(self.__function_list)
        if index>=fl_len: raise ListIndexOutOFRange(index,fl_len)
        self.__function_list[index].plot()

    def get_min(self, verbose=False) -> float:
        m = min((f.get_min(), idx) for idx, f in enumerate(self.__function_list))
        if verbose: print("The min value is: " + str(m[0]) + " from <" + str(self.__function_list[m[1]]) + "> PieceFunction")
        return m
    
    def get_max(self, verbose=False) -> float:
        m = max((f.get_max(), idx) for idx, f in enumerate(self.__function_list))
        if verbose: print("The max value is: " + str(m[0]) + " from <" + str(self.__function_list[m[1]]) + "> PieceFunction")
        return m

    def __str__(self) -> str:
        f_list_str = "[\n"
        for f in self.__function_list:
            f_list_str += str(f) + "\n"
        return f_list_str + "]"

    def report_f(self):
        print(self)
        self.plot()

    def plot(self):
        color_pool= cycle(list(colorstring))  #avoid 2 consecutive functions have the same color
        [f.plot(show=False,f_color=next(color_pool)) for f in self.__function_list]
        plt.show()

