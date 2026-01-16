import sys
import math
from math import sqrt


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return self.message

def find_distance(start, finish):
    return sqrt((finish[0] - start[0]**2 + (finish[1] - start[1])**2) + (finish[2] - start[2])**2)


def coordinate_system():
    print(f"=== Game Coordinate System ===")
    pos0 = (0,0,0)      #x1 y1 z1
    pos1 = (10,20,5)    #x2 y2 z2
    print(f"Position Created {pos1}")



if __name__ == "__main__":
    coordinate_system()
    pass