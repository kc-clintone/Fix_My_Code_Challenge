#!/usr/bin/python3

class square():
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Perimeter """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ str repr """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    sq = square(width=12, height=9)
    print(sq)
    print(sq.area_of_my_square())
    print(sq.PermiterOfMySquare())
