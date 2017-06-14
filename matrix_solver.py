""" matrix solver + latex printer
"""
from fractions import *


class Matrix:
    """ matrix class
    === Attributes ===
    @type arr: List
    @type augment: List
    @type cols: int
    @type rows: int
    @type c_cols: int
    @type c_rows: int
    @type latex: Bool
    """
    def __init__(self, arr, augment=None, latex=False):
        """
        create a new matrix

        @type self: Matrix
        @type arr: List
        @type augment: List | None
        @type latex: Bool
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

        @type self: Matrix
        @rtype: Matrix
        """
        x = 1
        # still needs to be implimeted

    def mutlipy_row(self, row_num, multiplier):
        """
        scaler multiply a row

        @type self: Matrix
        @type row_num: int
        @type multiplier: int
        @rtype: None | Print

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
        >>> c.mutlipy_row(1, Fraction(1,2))
        """
        for i in range(len(self.arr[row_num-1])):
            self.arr[row_num-1][i] = self.arr[row_num-1][i] * multiplier
        if self.augment is not None:
            for i in range(len(self.augment[row_num-1])):
                self.augment[row_num - 1][i] = (self.augment[row_num - 1][i] *
                                                multiplier)
        if self.latex:
            opertation = '\\xrightarrow[]{ '
            if (isinstance(multiplier, int) or
                multiplier.numerator % multiplier.denominator == 0):
                opertation += str(int(multiplier)) + 'r_' + str(row_num) + ' }'
            else:
                opertation += ('\\frac{' + str(multiplier.numerator) + '}{' +
                               str(multiplier.denominator) + '}' +
                               'r_' + str(row_num) + ' }')
            print(opertation)
            print(self)

    def add_rows(self, sign, row1_num, row2_num, multi1=1, multi2=1):
        """
        add/subtract(<sign>) a row <row1_num> by another one <row2_num>

        basic format : <multi1><row1_num>  <sign>  <multi2><row2_num>

        @type self: Matrix
        @type sign: str
        @type row1_num: int
        @type row2_num: int
        @type multi1: int
        @type multi2: int
        @rtype: None | Print

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
        >>> c.add_rows('-', 2, 1, Fraction(1,3), 1 )
        >>> c.arr
        """
        for i in range(len(self.arr[row1_num-1])):
            if sign == '+':
                self.arr[row1_num-1][i] = (multi1 * self.arr[row1_num-1][i] +
                                           multi2 * self.arr[row2_num-1][i])
            else:
                self.arr[row1_num-1][i] = (multi1 * self.arr[row1_num-1][i] -
                                           multi2 * self.arr[row2_num-1][i])

        if self.augment is not None:
            for i in range(len(self.augment[row1_num - 1])):
                if sign == '+':
                    self.augment[row1_num-1][i] = (multi1 *
                                                   self.augment[row1_num-1][i] +
                                                   multi2 *
                                                   self.augment[row2_num-1][i])
                else:
                    self.augment[row1_num-1][i] = (multi1 *
                                                   self.augment[row1_num-1][i] -
                                                   multi2 *
                                                   self.augment[row2_num-1][i])
        if self.latex:
            opertation = '\\xrightarrow[]{ '
            if (isinstance(multi1, int) or
                multi1.numerator % multi1.denominator == 0):
                opertation += (str(int(multi1)) + 'r_' + str(row1_num) +
                               ' ' + sign + ' ')
            else:
                opertation += (' \\frac{' + str(multi1.numerator) + '}{' +
                               str(multi1.denominator) + '}' +
                               'r_' + str(row1_num) + ' ' + sign + ' ')
            if (isinstance(multi2, int) or
                multi2.numerator % multi2.denominator == 0):
                opertation += (str(int(multi2)) + 'r_' + str(row2_num) +
                               ' \\rightarrow ' + ' r_' + str(row2_num) + ' }')
            else:
                opertation += (' \\frac{' + str(multi2.numerator) + '}{' +
                               str(multi2.denominator) + '} ' + 'r_' +
                               str(row2_num) + ' \\rightarrow ' + ' r_' +
                               str(row2_num) + ' }')
            print(opertation)
            print(self)

    def swap_rows(self, row1_num, row2_num):
        """
        swap 2 rows in a matrix

        @type row1_num: int
        @type row2_num: int
        @rtype: None | print

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
        >>> c.swap_rows(2, 1)

        """
        temp = self.arr[row1_num-1][:]
        self.arr[row1_num - 1] = self.arr[row2_num-1]
        self.arr[row2_num - 1] = temp

        if self.augment is not None:
            temp2 = self.augment[row1_num - 1][:]
            self.augment[row1_num - 1] = self.augment[row2_num - 1]
            self.augment[row2_num - 1] = temp2

        if self.latex:
            opertation = ('\\xrightarrow[]{ r_' + str(row1_num) +
                          ' \\leftrightarrow ' + 'r_' + str(row2_num) + ' }')
            print(opertation)
            print(self)

    def __str__(self):
        """
        latex string repsentation of a matirx

        @type self: Matrix
        @rtype: str

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
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
                                   str(j.denominator) + '} ' + ' & ')
            output = output[:-2] + ' \\\\  \n'
        output += '\\end{array} \n\\right]'
        return output


if __name__ == "__main__":
    import python_ta
    python_ta.check_all()
    import doctest
    doctest.testmod()
