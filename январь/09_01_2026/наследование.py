class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def avg(self):
        return (self.a + self.b) / 2


class B(A):
    def __init__(self, a, b, c):
        super().__init__(a,b)
        self.c = c

    def avg(self):
        print(super().avg())
        return (super().avg() + self.c) / 2


b = B(1,2,3)
print(b.avg())