import rational

class PowerSeries():

    def __init__(self, list_coefficients, accuracy=-1):
        """
        
        Args:
            list_coefficients (list of int): the list may only contain ints, any other type will
                raise an error in the Rational class
        
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
        if self.accuracy < len(self.coefficients) - 1:
            raise ValueError("Given accuracy is lower than the number of given coefficients.")
        else:
            self.coefficients = (
                self.coefficients
                 + [rational.Rational(0)] * (self.accuracy + 1 - len(self.coefficients))
            )



    @staticmethod
    def to_rational(list_coefficients):
        return [rational.Rational(coefficient) for coefficient in list_coefficients]



    def __str__(self):
        output_string = "("
        for rational in self.coefficients:
            output_string += str(rational) + ", "
        output_string = output_string[:-2] + ")"
        return output_string



if __name__ == "__main__":
    power1 = PowerSeries([1, 2, 3], 1)
    print(power1)
    print(power1.accuracy)