import math


class Vector3:
    def __init__(self, x=1, y=1, z=1):
        self.x = x
        self.y = y
        self.z = z

    @classmethod
    def from_list(cls, lst: list):
        return cls(lst[0], lst[1], lst[2])

    def to_list(self):
        return [self.x, self.y, self.z]

    @staticmethod
    def cross(v1, v2) -> "Vector3":
        """
        :type v1: Vector3
        :type v2: Vector3
        """
        r = Vector3()
        r.x = v1.y * v2.z - v1.z * v2.y
        r.y = v1.z * v2.x - v1.x * v2.z
        r.z = v1.x * v2.y - v1.y * v2.x

        return r

    @staticmethod
    def dot(v1, v2) -> int:
        """

        :type v1: Vector3
        :type v2: Vector3
        :rtype: int
        """
        return v1.x * v2.x + v1.y * v2.y + v1.z * v2.z

    def magnitude(self) -> float:
        r_square = self.x * self.x + self.y * self.y + self.z * self.z
        return math.sqrt(r_square)

    def __truediv__(self, other: int or float):
        if type(other) in [int, float]:
            return Vector3.from_list([x / other for x in self.to_list()])
        raise Exception("type error for divide of vector3")

    def __mul__(self, other: int or float):
        if type(other) in [int, float]:
            return Vector3.from_list([x * other for x in self.to_list()])
        raise Exception("type error for multiple of vector3")

    def __add__(self, other: "Vector3"):
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: "Vector3"):
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)

    def normalized(self) -> "Vector3":
        r = self / self.magnitude()
        return r


a = Vector3(1, 0, 0)
b = Vector3(0, 2, 0)
print(Vector3.cross(a, b).to_list())
