import math
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    def set_width(self, new_width):
        self.width = new_width
    def set_height(self, new_height):
        self.height = new_height
    
    def get_area(self):
        return self.width*self.height
    def get_perimeter(self):
        return 2*(self.width+self.height)
    def get_diagonal(self):
        return math.sqrt(math.pow(self.width, 2) + math.pow(self.height, 2))
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        line = "*" * self.width + "\n"
        return line * self.height
    def get_amount_inside(self, shape):
        cols = self.width // shape.width
        rows = self.height // shape.height
        return cols * rows

class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        
    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side
    def set_width(self, new_width):
        self.set_side(new_width)
    def set_height(self, new_height):
        self.set_side(new_height)

#testing
rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))