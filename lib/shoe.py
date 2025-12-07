APPROVED_SIZES = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

class Shoe:
    def __init__(self, brand="Adidas", size=9):
        self.brand = brand
        self.size = size
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if value in APPROVED_SIZES:
            self._size = value
        else:
            print("size must be an integer")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
