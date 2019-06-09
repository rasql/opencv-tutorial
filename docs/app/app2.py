import numpy as np

class Vec2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = x

    def __str__(self):
        return 'Vec2({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)

a = Vec2(1, 2)
b = Vec2(3, 4)

x = np.array((1, 2))
y = np.array((3, 4))


print(a + b)
print(x + y)
print(x.dtype)