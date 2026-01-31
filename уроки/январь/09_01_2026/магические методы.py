'''class A:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Str: {self.value}'

    def __del__(self):
         print(f'Del: {self.value}')

a = A(10)
a.value = 20
print(a.value)
print(a)
'''
class B:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ne__(self, other):
        return self.value != other.value

b1 = B(20)
b2 = B(20)
print(b1 == b2)
print(b1 < b2)
print(b1 > b2)
print(b1 <= b2)
print(b1 >= b2)
print(b1 != b2)


class C:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return C(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return C(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return C(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return C(self.x / other.x, self.y / other.y)

    def __abs__(self):
        return C(self.x ** 2 + self.y ** 2)

v1 = C(1, 2)
v2 = C(2, 3)
v3 = v1 + v2
print(v3.x)
print(v3.y)
