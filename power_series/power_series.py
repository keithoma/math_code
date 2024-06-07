import rational

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
        self.increase_accuracy(accuracy)
            



    @staticmethod
    def to_rational(list_coefficients):
        """
        
        Args:
            list_coefficients (list of int):
        
        Returns:
            (list of Rational):
        
        """
        return [rational.Rational(coefficient) for coefficient in list_coefficients]



    def __str__(self):
        """ Converts the list of coefficients as a readable string. Current format is
            (0, 1, 2).
        
        
        """
        output_string = "("
        for rational in self.coefficients:
            output_string += str(rational) + ", "
        output_string = output_string[:-2] + ")"
        return output_string



    def increase_accuracy(self, accuracy):
        if self.accuracy > accuracy:
            raise ValueError("You don't want to decrease accuracy, do you?")
        elif self.accuracy == accuracy:
            pass
        else:
            self.coefficients = (
                self.coefficients
                 + [rational.Rational(0)] * (self.accuracy + 1 - len(self.coefficients))
            )
        return self.accuracy


    def cauchy_product(self, right):
        self.accuracy = max(self.accuracy, right.accuracy)

        if len(b) > n: n = len(b)

        while len(a) < n: a.append(0)
        while len(b) < n: b.append(0)

        def c(k): return sum([a[l] * b[k - l] for l in range(k + 1)])

        return [c(k) for k in range(n)]



if __name__ == "__main__":
    power1 = PowerSeries([1, 2, 3], 1)
    print(power1)
    print(power1.accuracy)