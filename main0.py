from main0 import Rectangle

class Square(Rectangle):
    def __init__(self, side_length) -> None:
        self.length = side_length
        self.width = side_length
        super().__init__(length=side_length, width=side_length)
     
if __name__ == "__main__":
    square = Square(side_length=2)
    print("Information about the first rectangle")
    print("Length: ", square.length)
    print("Width: ", square.width)
    print("Area: ", square.area())
    print("Perimeter: ", square.perimeter())
