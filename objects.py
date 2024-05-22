class Operation:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.result = self.op()

    def op(self):
        return self.a + self.b

    def __add__(self, other):
        return self.result + other.result

    def __mul__(self, other):
        return self.result * other.result

    def __sub__(self, other):
        return self.result - other.result


class Add(Operation):
    def op(self):
        return self.a + self.b

    def __str__(self):
        return f"({self.a} + {self.b})"

    def __repr__(self):
        return f"Add({self.a}, {self.b})"


class Mul(Operation):
    def op(self):
        return self.a * self.b

    def __str__(self):
        return f"({self.a} * {self.b})"

    def __repr__(self):
        return f"Mul({self.a}, {self.b})"


class Sub(Operation):
    def op(self):
        return self.a - self.b

    def __str__(self):
        return f"({self.a} - {self.b})"

    def __repr__(self):
        return f"Sub({self.a}, {self.b})"
