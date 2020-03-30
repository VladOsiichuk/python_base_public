class Polygon:
    def __init__(self, no_of_sides):
        self.name = None
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def get_sides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def show_sides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

    def show_result(self, result):
        print(f"The area of {self.name} is ", result)

class Triangle(Polygon):
    def __init__(self):
        super().__init__(3)
        self.name = "triangle"

    def find_area(self):
        a, b, c = self.sides
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        self.show_result(area)


class Square(Polygon):
    def __init__(self):
        super().__init__(1)
        self.name = "square"

    def find_area(self):
        side = self.sides[0]
        area = side ** 2
        self.show_result(area)

    def get_triangle(self, triangle):
        print(triangle.sides)

triangle = Triangle()
triangle.get_sides()
triangle.find_area()
square = Square()

square.get_triangle(triangle)

square.get_sides()
square.find_area()