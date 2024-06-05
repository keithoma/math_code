import rational

class PowerSeries():

    def __init__(self, list_coefficients):
        """
        
        Args:
            list_coefficients (list of int): the list may only contain ints, any other type will
                raise an error in the Rational class
        
        """
        self.coefficients = PowerSeries.to_rational(list_coefficients)

    @staticmethod
    def to_rational(list_coefficients):
        return [rational.Rational(coefficient) for coefficient in list_coefficients]
