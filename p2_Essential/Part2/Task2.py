class Figure:
    def __init__(self, side=0.0):
        self.side = side

class Square(Figure):
    def draw(self):
        for i in range(self.side):
            print('* ' * self.side)

class Triangle(Figure):
    def draw(self):
        for i in range(1, self.side + 1):
            print('* ' * i)

def main():
    square = Square(6)
    triangle = Triangle(8)
    square.draw()
    triangle.draw()

if __name__ == '__main__':
    main()