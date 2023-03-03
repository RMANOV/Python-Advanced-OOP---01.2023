# Stack of Strings
# Create a class Stack that can store only strings and has the following functionality:
# •	Instance attribute: data: list
# •	Method: push(element) – adds an element at the end of the stack
# •	Method: pop() – removes and returns the last element in the stack
# •	Method: top() - returns a reference to the topmost element of the stack
# •	Method: is_empty() - returns boolean True/False
# •	Override the string method to return the stack data in the format:
# "[{element(N)}, {element(N-1)} ... {element(0)}]"

from typing import List

class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self) -> str:
        return self.data[-1]

    def is_empty(self) -> bool:
        return not self.data

    def __str__(self):
        return "[" + ", ".join(self.data[::-1]) + "]" if self.data else "[]"