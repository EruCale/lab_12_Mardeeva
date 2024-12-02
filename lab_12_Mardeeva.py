#Task1
class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return self.__format_time()

    def __format_time(self):
        return f"{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}"

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.previous_second()
print(timer)

#Task2
class WeekDayError(Exception):
    pass


class Weeker:
    __days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    def __init__(self, day):
        if day not in self.__days:
            raise WeekDayError(f"Invalid day: {day}")
        self.__current_day_index = self.__days.index(day)

    def __str__(self):
        return self.__days[self.__current_day_index]

    def add_days(self, n):
        self.__current_day_index = (self.__current_day_index + n) % len(self.__days)

    def subtract_days(self, n):
        self.__current_day_index = (self.__current_day_index - n) % len(self.__days)

try:
    weeker = Weeker("Tue")
    print(weeker)
    weeker.add_days(3)
    print(weeker)
    weeker.subtract_days(5)
    print(weeker)
    weeker = Weeker("Funday")
except WeekDayError as e:
    print(e)

#Task3
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

point1 = Point(3, 4)
point2 = Point(0, 0)

print("Координати точки 1:", point1.getx(), point1.gety())
print("Координати точки 2:", point2.getx(), point2.gety())

print("Відстань від точки 1 до (0, 0):", point1.distance_from_xy(0, 0))
print("Відстань між точками 1 і 2:", point1.distance_from_point(point2))

#Task4
class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        p1, p2, p3 = self.__points
        side1 = p1.distance_from_point(p2)
        side2 = p2.distance_from_point(p3)
        side3 = p3.distance_from_point(p1)
        return side1 + side2 + side3

point_a = Point(0, 0)
point_b = Point(3, 0)
point_c = Point(0, 4)

triangle = Triangle(point_a, point_b, point_c)

print("Периметр трикутника:", triangle.perimeter())