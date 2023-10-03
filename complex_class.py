import math
from math import hypot


class Complex:
    print("The first line announces our start to work with complex numbers")

    ###########################################################################

    def __init__(self, real=None, image=None):
        self.real = 0
        self.image = 0
        if type(real) is str:
            inPutStr = real  # Стоит задача определения знаков! Мы научились принимать последовательность!!!
            inPutStr = inPutStr.replace(' ', '')
            inPut = inPutStr.replace(' ', '')
            inPut = inPut.split('-')
            nums = []
            for num in range(len(inPut)):
                nums += inPut[num].split('+')

            for num in nums:
                if num != '':
                    if 'i' in num:
                        if inPutStr.find(num) > 0:
                            if inPutStr[inPutStr.find(num) - 1] == '-':
                                self.image -= int(num[0:-1], 10)
                            else:
                                self.image += int(num[0:-1], 10)
                        else:
                            self.image += int(num[0:-1], 10)
                    else:
                        if inPutStr.find(num) > 0:
                            if inPutStr[inPutStr.find(num) - 1] == '-':
                                self.real -= int(num, 10)
                            else:
                                self.real += int(num, 10)
                        else:
                            self.real += int(num, 10)

        else:
            self.real = real
            self.image = image

    ###########################################################################

    # REPR STR

    def __repr__(self):
        return f"Complex({self.real},{self.image})"

    def __str__(self):
        if self.real is None and self.image is None:
            self.real = 0
            return f"{self.real}"
        elif self.real is not None and self.image is None:
            # self.image = 0 # Нельзя вводить!!! Будет ошибка в EQ
            return f"{self.real}"
        elif self.real is None and self.image is not None:
            self.real = 0
            return f"{self.image}"
        else:
            if self.real != 0 and self.image != 0:
                if self.image > 0:
                    return f"{self.real} + {self.image}i"
                else:
                    return f"{self.real} - {-self.image}i"
            elif self.image != 0 and self.real == 0:
                return f"{self.image}i"
            elif self.image == 0 and self.real != 0:
                return f"{self.real}"
            elif self.real == 0 and self.image == 0:
                return f"{self.real} + {self.image}i"

    ###########################################################################

    # ADD RADD IADD
    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.image + other.image)
        else:
            return Complex(self.real + other, self.image)

    def __radd__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.image + other.image)
        else:
            return Complex(self.real + other, self.image)

    def __iadd__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real + other.real, self.image + other.image)
        else:
            return Complex(self.real + other, self.image)

    ###########################################################################

    # MUL RMULL IMULL
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.image * other.image, \
                           self.image * other.real + self.real * other.image)
        else:
            return Complex(self.real * other, self.image * other)

    def __rmul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.image * other.image, \
                           self.image * other.real + self.real * other.image)
        else:
            return Complex(self.real * other, self.image * other)

    def __imul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real * other.real - self.image * other.image, \
                           self.image * other.real + self.real * other.image)
        else:
            return Complex(self.real * other, self.image * other)

    ###########################################################################

    # SUB RSUB ISUB
    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.image - other.image)
        else:
            return Complex(self.real - other, self.image)

    def __rsub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.image - other.image)
        else:
            return Complex(self.real - other, self.image)

    def __isub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.real - other.real, self.image - other.image)
        else:
            return Complex(self.real - other, self.image)

    ###########################################################################

    def __truediv__(self, other):
        if isinstance(other, Complex):
            pass
        else:
            return Complex(self.real / other, self.image / other)

    # NEG POS BOOL
    def __neg__(self):
        return Complex(-self.real, -self.image)

    def __pos__(self):
        return Complex(self.real, self.image)

    def __bool__(self):
        if self.real == 0 and self.image == 0:
            return False
        else:
            return True

    ###########################################################################
    ##
    # EQ NE
    # Необходимо понимать, что мы хотим сравнивать комплексные числа, как
    # с комплексными числами, так и с целыми!
    def __eq__(self, other):
        if isinstance(other, Complex):
            if self.real is None:
                self.real = 0
            if self.image is None:
                self.image = 0
            if other.image is None:
                other.image = 0
            if other.real is None:
                other.real = 0
            if self.real == other.real and self.image == other.image:
                return True
            else:
                return False
        else:  # Решено
            if self.image is not None and self.image != 0:
                return False
            elif (self.real is None and self.image is None) and other == 0:
                return True
            elif self.real != 0 and self.real != other:
                return False
            elif self.real == other:
                return True

    def __ne__(self, other):
        if not self == other:
            return True
        else:
            return False

    ###########################################################################

    def __abs__(self):
        return hypot(self.real, self.image)

    ###########################################################################

    # PHASE(z) POLAR(z) RECT(r, phi)

    def phaze(self):
        return math.atan2(self.image, self.real)

    def polar(self):
        return f'Z: {self} \nR: {abs(self)} \nphi: {self.phaze()}'


a = Complex('2 + 3i +5')

print(print(a + 2 + Complex(0, 3)))
