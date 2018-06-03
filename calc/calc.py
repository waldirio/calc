""" Calc code example """


class Calc():
    """ Calculator Class """

    def sum_call(self, first, second):
        """ Sum Def """
        return first + second

    def div_call(self, first, second):
        """ Div Def """
        return first/second

    def mult_call(self, first, second):
        """ Mult Def """
        return first*second

    def subs_call(self, first, second):
        """ Subs Def """
        return first-second


def main():

    # Object creation
    n1 = Calc()

    # Sum of 2 and 3
    aux = n1.sum_call(2, 3)
    print("Sum of 2 + 3 is: " + str(aux))

    # Division of 10 and 5
    aux = n1.div_call(10, 2)
    print("Division of 10 / 5 is: " + str(aux))

    # Multiplication of 2 and 10
    aux = n1.mult_call(2, 10)
    print("Multiplication of 2 * 10 is: " + str(aux))

    # Subtraction of 100 and 30
    aux = n1.subs_call(100, 30)
    print("Subtraction of 100 - 30 is: " + str(aux))


if __name__ == '__main__':
    main()
