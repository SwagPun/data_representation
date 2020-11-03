# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class BinaryString:
    def __init__(self, binary):
        self.value = binary

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        if type(value) != str:
            raise ValueError("Binary string given must be a string")
        for digit in value:
            if digit not in ["1", "0"]:
                raise ValueError("Binary string given contains values that are not 1 or 0")
        self.__value = value

    def __str__(self):
        return self.value


class FloatingPointNumber(BinaryString):
    def __init__(self, mantissa, exponent):
        super().__init__(mantissa+exponent)
        self.mantissa_size = len(mantissa)
        self.exponent_size = len(exponent)

    @classmethod
    def as_single_string(cls, binary, mantissa_size):
        return cls(binary[:mantissa_size], binary[mantissa_size:])




if __name__ == '__main__':
    x = FloatingPointNumber("010101", "001")
    y = FloatingPointNumber.as_single_string("010101001", 6)
    print(x, y)


