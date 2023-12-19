#!/usr/bin/python3

class Square:
    
    def __init__(self, width: float = 0, height: float = 0, **kwargs):
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self) -> float:
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self) -> float:
        """ Perimeter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self) -> str:
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
