from calc.calc import Calc

def test_sum():
    n1 = Calc(3,6)
    assert n1.sum_call() == 9

