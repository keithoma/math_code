""" Note to my future self: PowerSeries.cauchy_product is not working ... it must be because
I'm trying to use sum() on rational object ...

Implements the PowerSeries class that represents a power series. A mathematical power series has
infinitely many coefficients, i.e. all polynomials may be viewed as a power series with almost all
coefficients being zero, but obviously we cannot save infinitely many coefficients. Thus, the
PowerSeries class defines an attribute called 'accuracy' that sets how many of the first
coefficients we will care about. The coefficients themselves are saved as a list of Rational
objects (see rational.py) in the attribute 'coefficients'.
"""


from rational import Rational

class PowerSeries():

    def __init__(self, list_coefficients, accuracy=-1):
        """
        
        Args:
            list_coefficients (list of int): the list may only contain ints, any other type will
                raise an error in the Rational class
            
            accuracy (int): the number of the first coefficients we want to look at, the 0-th
                coefficient is the constant coefficient, the first is the coefficient of X^1 and so
                on

                Negative values will be overwritten by the number of coefficients given. Thus, if
                no argument is given for accuracy, we will take the number of coefficients given as
                accuracy.
        
        """
        self.coefficients = PowerSeries.to_rational(list_coefficients)
        
        # a power series has infinitely many coefficients, but we cannot save them all of course,
        # the attribute accuracy indicates how many of the first coefficients we want to look
        # 
        # the constant coefficient is the 0-th coefficient, a_1 X^1 is the first, so on and so on
        if not isinstance(accuracy, int): raise TypeError("Accuracy must be an integer.")

        if accuracy < 0:
            self.accuracy = len(self.coefficients) - 1
        else:
            self.accuracy = accuracy

        # make sure the number of coefficients matches our accuracy
        self.match_accuracy_to(self.accuracy)
            



    @staticmethod
    def to_rational(list_coefficients):
        """
        
        Args:
            list_coefficients (list of int):
        
        Returns:
            (list of Rational):
        
        """
        return [Rational(coefficient) for coefficient in list_coefficients]



    def __str__(self):
        """ Converts the list of coefficients as a readable string. Current format is
            (0, 1, 2).
        
        
        """
        output_string = "("
        for rational in self.coefficients:
            output_string += str(rational) + ", "
        output_string = output_string[:-2] + ")"
        return output_string

    def match_accuracy_to(self, accuracy=None):
        """
        """
        # if a value was given for accuracy, update the attribute
        if accuracy is not None:
            self.accuracy = accuracy
        
        # append 0s as Rational objects at the end of the coefficients
        self.coefficients = (
            self.coefficients
            + [Rational(0)] * (self.accuracy + 1 - len(self.coefficients))
        )
        return self


    def cauchy_product(self, right):
        self.accuracy = right.accuracy = max(self.accuracy, right.accuracy)
        self.match_accuracy_to()

        print("-----------")
        print(self.accuracy)
        print(right.accuracy)
        print("-----------")

        def c(k):
            return Rational.rational_sum(
                [self.coefficients[l] * right.coefficients[k - l] for l in range(k + 1)]
            )

        return PowerSeries([c(k) for k in range(self.accuracy + 1)])



if __name__ == "__main__":
    power1 = PowerSeries([1, 2, 3])
    power2 = PowerSeries([1, 0, -1, 2])
    # print(power1.accuracy)
    # print("------------")
    # print(power1)
    # print(power2)
    cauchy = power1.cauchy_product(power2)
    print(cauchy)
    # print(cauchy.accuracy)
