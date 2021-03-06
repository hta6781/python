"""
Write a modified version of the Matrix class(that was defined in
one of the example problems in this section) so that the __str__
method instead returns a string containing a single number: the
matrix's Frobenius norm. The formula for the Frobenius norm will
be the square root of the sum of all the elements squared in the
matrix. Also, the unmodified Matrix class code will be given.
"""

# write your code below

import math

"""
This is the unmodified Matrix class code.

class Matrix:
   def __init__(self,thelist: list):
       self.thelist=thelist
       for items in range(len(self.thelist)):
           assert type(self.thelist[items]) == list
           assert len(self.thelist[0]) == len(self.thelist[items])
           for things in range(len(self.thelist[items])):
               assert type(self.thelist[items][things]) == int

   def __str__(self):
       return str(self.thelist)
"""


class Matrix:
    def __init__(self, thelist: list):
        self.thelist = thelist
        for items in range(len(self.thelist)):
            assert type(self.thelist[items]) == list
            assert len(self.thelist[0]) == len(self.thelist[items])
            for things in range(len(self.thelist[items])):
                assert type(self.thelist[items][things]) == int
        self.froebiannorm()

    def froebiannorm(self):
        self.squared = 0
        for items in range(len(self.thelist)):
            for things in range(len(self.thelist[items])):
                self.squared += self.thelist[items][things] ** 2
        self.norm = math.sqrt(self.squared)

    def __str__(self):
        return str(self.norm)


mymatrix = Matrix([[3, 4], [7, 8]])
print(str(mymatrix))
