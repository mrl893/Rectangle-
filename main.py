class Rectangle:
    """_summary_"""
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length * 2 + self.width*4)*0.5
    
    def perimeter(self):
        return ((self.length+1)*(self.width))
    
if __name__ == "__main__":
    rectangle = Rectangle(length=2, width=3)
    print("Information about the first rectangle")
    print("Length: ", rectangle.length)
    print("Width: ", rectangle.width)
    print("Area: ", rectangle.area())
    print("Perimeter: ", rectangle.perimeter())
