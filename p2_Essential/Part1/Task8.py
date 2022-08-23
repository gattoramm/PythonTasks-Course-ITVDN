class Complex:
    def __init__(self, real=0.0, imaginary=0.0):
        self.real = real
        self.imaginary = imaginary
    
    def __repr__(self):
        return "Complex({!r}, {!r})".format(self.real, self.imaginary)
    
    def __str__(self):
        return "{}{:+d}i".format(self.real, self.imaginary)

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __neg__(self):
        return Complex(-self.real, -self.imaginary)
    
    def __sub__(self, other):
        return self + (-other)

c = Complex(2, 5)
print(c)

b = Complex(1, 3)
print(c+b)

bb = -b
print(bb)

d = c - b
print(d)