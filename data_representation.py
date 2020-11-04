# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class BinaryString:
    def __init__(self, binary):
        self.value = binary

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if type(value) != str:
            raise ValueError("Binary string given must be a string")
        for digit in value:
            if digit not in ["1", "0"]:
                raise ValueError("Binary string given contains values that are not 1 or 0")
        self._value = value

    def __str__(self):
        return self.value

    def __add__(self, other):
        return BinaryString(str(self) + str(other))

    def __len__(self):
        return len(self.value)

    def __invert__(self):
        inverted = ""
        for bit in self.value:
            if bit == "1":
                inverted += "0"
            else:
                inverted += "1"
        return inverted


class FixPointNumber(BinaryString):
    def __init__(self, binary, point):
        if type(point) != int:
            raise ValueError("The argument <point> must be a whole number")
        self._binary_point = point
        super(FixPointNumber, self).__init__(binary)

    def __float__(self):
        column_value = 2 ** (len(self)-1)
        total = 0
        for bit in self.value:
            total += int(bit) * column_value
            column_value /= 2
        total = total * (2**(self._binary_point-len(self)))
        return total

    def __int__(self):
        return int(float(self))

    def __str__(self):
        if self._binary_point < len(self):
            return self.value[:self._binary_point] + "." + self.value[self._binary_point:]
        else:
            return self.value


class TwosComplementNumber(BinaryString):
    def __abs__(self):
        """ Returns whole number part of twos complement number as BinaryString"""
        pass

    def to_positive(self):
        pass

    def __neg__(self):
        pass

    def is_positive(self):
        pass

    def is_negative(self):
        pass


class FloatingPointNumber():
    def __init__(self, mantissa, exponent):
        self.mantissa = BinaryString(mantissa)
        self.exponent = BinaryString(exponent)

    @classmethod
    def as_single_string(cls, binary, mantissa_size):
        return cls(binary[:mantissa_size], binary[mantissa_size:])

    @property
    def mantissa(self):
        return self._mantissa

    @mantissa.setter
    def mantissa(self, mantissa):
        self._mantissa = mantissa

    @property
    def exponent(self):
        return self._exponent

    @exponent.setter
    def exponent(self, exponent):
        self._exponent = exponent

    def __str__(self):
        return str(self.mantissa + self.exponent)

    def __int__(self):

        #Convert exponent from twos complement

        #Convert to integer

        #Convert mantissa from twos complement

        #Convert to integer
        pass


if __name__ == '__main__':
    x = FloatingPointNumber("011", 3)
    print(x)
    print(~x)


