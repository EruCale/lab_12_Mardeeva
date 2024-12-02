#Task2.1
class WeekDayError(Exception):
    pass


class Weeker:
    DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        if day not in self.DAYS:
            raise WeekDayError
        self._day = day

    def __str__(self):
        return self._day

    def add_days(self, n):
        current_index = self.DAYS.index(self._day)
        new_index = (current_index + n) % 7
        self._day = self.DAYS[new_index]

    def subtract_days(self, n):
        current_index = self.DAYS.index(self._day)
        new_index = (current_index - n) % 7
        self._day = self.DAYS[new_index]


try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")



#Task3.1
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self._x = x
        self._y = y

    def getx(self):
        return self._x

    def gety(self):
        return self._y

    def distance_from_xy(self, x, y):
        return math.hypot(self._x - x, self._y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())

point1 = Point(0, 0)
point2 = Point(1, 1)
print(point1.distance_from_point(point2))  # Очікуваний вивід: 1.4142135623730951
print(point2.distance_from_xy(2, 0))       # Очікуваний вивід: 1.4142135623730951


#Task4.1
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])
        return side1 + side2 + side3


# Test the code
point1 = Point(0, 0)
point2 = Point(1, 1)
point3 = Point(1, 0)

triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())  # Очікуваний вивід: 3.414213562373095



