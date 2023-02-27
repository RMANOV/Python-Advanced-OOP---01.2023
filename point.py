# Point
# Create a class called Point. Upon initialization, it should receive x and y (numbers). Create 3 instance methods:
# -	set_x(new_x) - changes the x value of the point
# -	set_y(new_y) - changes the y value of the point
# -	__str__() - returns the coordinates of the point in the format "The point has coordinates ({x},{y})"

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def __str__(self):
        return f"The point has coordinates ({self.x},{self.y})"


p = Point(2, 4)
print(p)
p.set_x(3)
p.set_y(5)
print(p)
