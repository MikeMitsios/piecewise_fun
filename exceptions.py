class WrongType(TypeError):

    def __init__(self, variable_name, variable_type, type) -> None:
        self.type = type
        self.message = "<" + variable_name + "> should be " + type + ". Instead got: " + str(variable_type)
        super().__init__( self.message)

class OutOfRange(ValueError):

    def __init__(self,x, fun) -> None:
        self.x = x
        self.message = "Value: " + str(self.x) + " is out of functions range < " + str(fun)+ " >"
        super().__init__( self.message) 

class RangeError(ValueError):

    def __init__(self, start, end) -> None:
        self.message = "start(" + str(start) + ") should be less than or equal to end(" + str(end) + ")"
        super().__init__(self.message)


class FunctionFormat(ValueError):

    def __init__(self, fun) -> None:
        self.message = "Function formula "+fun+" must not include other parameter except x"
        super().__init__(self.message)


class RangeInconsistency(ValueError):

    def __init__(self, index1, item1, index2, item2 ) -> None:
        self.message = "function_list item ["+str(index1)+"] <"+ item1 +"> and ["+str(index2)+"] <"+ item2 +"> must not share values of their domains"
        super().__init__(self.message)


class ListIndexOutOFRange(IndexError):

    def __init__(self, index, len) -> None:
        self.message = "List index ("+str(index)+") is out of range of PiecewiseFunction (len = "+str(len)+")"
        super().__init__(self.message)