# Glass
# Create a class called Glass. Upon initialization, it will not receive any parameters. 
# You must create an instance attribute called content which should be equal to 0. 
# You should also create a class attribute called capacity which should be 250 ml. Create 3 instance methods:
# -	fill(ml) - fills the glass with the given milliliters if there is enough space in it and returns "Glass filled with {ml} ml", 
# otherwise returns "Cannot add {ml} ml"
# -	empty() - empties the glass and returns "Glass is now empty" 
# -	info() - returns info about the glass in the format "{space_left} ml left"


class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if self.content + ml <= self.capacity:
            self.content += ml
            return f"Glass filled with {ml} ml"
        return f"Cannot add {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"