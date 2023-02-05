#!/usr/bin/python3

class Square:
    """Class to represent a Square.
    
    Attributes:
    size (int): The size of the square.
    position (tuple): A tuple representing the position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a given size and position.
        
        Args:
        size (int): The size of the square. Default is 0.
        position (tuple): A tuple representing the position of the square. Default is (0, 0).
        
        """
        self.size = size
        self.position = position
        
    def area(self):
        """Return the area of the square."""
        return self.size ** 2

    def my_print(self):
        """Print the square to the standard output."""
        if self.size == 0:
            print()
        else:
            for i in range(self.position[1]):
                print()
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
