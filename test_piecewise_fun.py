from piecewise_fun import PieceFunction as pf, PiecewiseFunction as pwf
import pytest 
from exceptions import WrongType, RangeError, FunctionFormat, RangeInconsistency, OutOfRange


def test_functions_creation():
    f1=pf(0,1,(True,False), "3*x")
    assert f1.start==0 and f1.end==1 and f1.function=="3*x" and f1.equal==(True,False)

def test_wrong_input():
    with pytest.raises(WrongType):
        f1=pf("0",1,("ads",219), 3)
    
def test_wrong_fun_format():
    with pytest.raises(FunctionFormat):
        f1=pf(0,1,(True,False), "H+e-ll==o")

def test_evaluation():
    f1=pf(-1,5,(True,False), "3*x")
    assert f1.eval(3)==9
    
def test_out_of_range_evaluation():
    with pytest.raises(OutOfRange):
        f1=pf(-1,1,(True,False), "5*x")
        assert f1.eval(3)==9

def test_min_value():
    f1=pf(-1,1,(True,False), "5*x")
    assert f1.get_min()==-5

def test_max_value():
    f1=pf(-1,1,(True,False), "-5*x")
    assert f1.get_max()==5

def test_pw_function_creation():
    f1=pf(0,1,(True,False), "3*x")
    f2=pf(1,3, (False, False), "10")
    pwf_list=pwf( [f1,f2])
    assert pwf_list.get_fun(0)==f1 and pwf_list.get_fun(1)==f2

def test_pw_function_range_intersection():
    with pytest.raises(RangeInconsistency):
        f1=pf(0,2,(True,False), "3*x")
        f2=pf(1,3, (False, False), "10")
        pwf_list=pwf( [f1,f2])
        assert pwf_list.get_fun(0)==f1 and pwf_list.get_fun(1)==f2

def test_pwf_evaluation():
    f1=pf(0,3,(True,True), "3*x")
    f2=pf(3,10, (False, False), "10")
    pwf_list=pwf( [f1,f2])
    assert pwf_list.eval(3)==9 and pwf_list.eval(5)==10

def test_add_fun_to_pwf():
    f1=pf(0,3,(True,True), "3*x")
    f2=pf(3,10, (False, False), "10")
    pwf_list=pwf( [f1,f2])
    f3=pf(10,16, (True, False), "2*x+5")
    pwf_list.add_fun(f3)
    assert pwf_list.get_fun(2)==f3 and len(pwf_list)==3

def test_remove_fun_from_pwf():
    f1=pf(0,3,(True,True), "3*x")
    f2=pf(3,10, (False, False), "10")
    f3=pf(10,16, (True, False), "2*x+5")
    pwf_list=pwf( [f1,f2, f3])
    pwf_list.remove_fun(2)
    assert pwf_list.get_fun(0)==f1 and pwf_list.get_fun(1)==f2 and len(pwf_list)==2

def test_pwf_min():
    f1=pf(0,3,(True,True), "3*x")
    f2=pf(3,10, (False, False), "10")
    pwf_list=pwf( [f1,f2])
    min, argmin=pwf_list.get_min()
    assert min==0 and argmin==0

def test_pwf_max():
    f1=pf(0,3,(True,True), "3*x")
    f2=pf(3,10, (False, False), "10")
    pwf_list=pwf( [f1,f2])
    max, argmax= pwf_list.get_max()
    assert max==10 and argmax==1