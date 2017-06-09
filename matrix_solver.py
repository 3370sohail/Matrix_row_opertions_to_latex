""" matrix solver + latex printer
"""


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



    def __str__(self):
        """
        latex string repsentation of a matirx

        \left[
        \begin{array}{ccc|c}
        -1 &  3 & 1 & 1 \\
        3 &  1 & 1 & 2\\
        0 &  2 & 1 & 4 \\
        1 &  0 & 1 & 0\\
        \end{array}
        \right]

        @rtype: str

        >>> c = Matrix([[1, 2], [3, 4]], [[1],[2]], True )
        >>> print(c)
        ''
        """
        output = '\\left[ \n\\begin{array}{' + self.cols*'c'
        if self.c_cols >= 1:
            output += '|' + self.c_cols*'c'
        output += '} \n'

        for index, row in enumerate(self.arr):
            for i in row:
                output += str(i) + ' & '
            if self.c_cols >= 1:
                for j in self.augment[index]:
                    output += str(j) + ' & '
            output = output[:-2] + ' \\\\  \n'
        output += '\\end{array} \n\\right]'
        return output

def REF(arr, augment):

def RREF():




if __name__ == "__main__":
    import python_ta
    python_ta.check_all(config='pylint.txt')
    import doctest
    doctest.testmod()
