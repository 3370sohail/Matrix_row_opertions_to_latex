""" matrix solver + latex printer
"""
from fractions import *

class Matrix:
    """ matrix class
    === Attributes ===
    """
    def __init__(self, arr, augment, latex):
        """
        creat a new matrix

        @rtype: None
        """
        self.arr = arr
        self.augment = augment
        self.rows = len(arr)
        self.cols = len(arr[0])
        self.c_rows = len(augment)
        self.c_cols = len(augment[0])
        self.latex = latex

    def solve(self):
        """
        sovle matrix

        @rtype: Matrix
        """
        x = 1

    def mutlipy_row(self, row_num, multiplier):
        """
        scaler multiply a row
        @rtype: None | Print
        >>> a = Fraction(2,1)
        >>> b = Fraction(21,13)
        >>> print(a.numerator%a.denominator , type(a+a), int(1))
        """
        for i in range(len(self.arr[row_num-1])):
            self.arr[row_num-1][i] = self.arr[row_num-1][i] * multiplier

        if self.latex:
            opertation = '\\xrightarrow[]{'
            if (isinstance(multiplier, int) or
                multiplier.numerator % multiplier.denominator == 0):
                opertation += str(int(multiplier)) + 'r_' + str(row_num) + '}'
            else:
                opertation += ('\\frac{' + str(multiplier.numerator) + '}{' +
                               str(multiplier.denominator) + '}' +
                               'r_' + str(row_num) + '}')
            print(opertation)
            print(self)

    def __str__(self):
        """
        latex string repsentation of a matirx

        @rtype: str

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
        >>> c.mutlipy_row(1, Fraction(1,2))
        >>> print(c)
        \left[
        \begin{array}{cc|c}
        1 & 2 & 1  \\
        3 & 4 & 2  \\
        \end{array}
        \right]
        }{}
        """
        output = '\\left[ \n\\begin{array}{' + self.cols*'c'
        if self.c_cols >= 1:
            output += '|' + self.c_cols*'c'
        output += '} \n'

        for index, row in enumerate(self.arr):
            for i in row:
                if isinstance(i, int) or i.numerator % i.denominator == 0:
                    output += str(int(i)) + ' & '
                else:
                    output += ('\\frac{' + str(i.numerator) + '}{' +
                               str(i.denominator) + '}' + ' & ')
            if self.c_cols >= 1:
                for j in self.augment[index]:
                    if isinstance(j, int) or j.numerator % j.denominator == 0:
                        output += str(int(j)) + ' & '
                    else:
                        output += ('\\frac{' + str(j.numerator) + '}{' +
                                   str(j.denominator) + ' & ')
            output = output[:-2] + ' \\\\  \n'
        output += '\\end{array} \n\\right]'
        return output

#def REF(arr, augment):

#def RREF():




if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
