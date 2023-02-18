#!/usr/bin/python3
"""1-square.py: Python script that defines square,
   private instantiation attribute of size"""


class Square:

    """Creates  Square type"""
    def __init__(self, size):
        """ Initializes Square with size with,
        no type/value verification"""
        self.__size = size
