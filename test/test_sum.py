import sys

sys.path.insert(0,'/home/wpinheir/code/calc/calc')

from calc import *

def test_sum():
    n1 = Calc()
    assert n1.sum_call(3,6) == 9

