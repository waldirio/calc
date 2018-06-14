import unittest
from calc.calc import Calc

class TestDiv(unittest.TestCase):
    def test_div(self):
        #self.assertEquals(1,1)
        
        n1 = Calc(2,2)
        self.assertEquals(n1.div_call(),1)
