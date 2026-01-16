import sys


from math import sqrt


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return self.message

def find_distance(start, finish):
    return sqrt((finish[0] - start[0])**2 + (finish[1] - start[1])**2 + (finish[2] - start[2])**2)


def coordinate_system(coordinates):
    if len(coordinates) != 3:
        return print(f"Error: Invalid number of arguments. Usage python3 coordinate_system.py 'distance' '2,3,5' ")
    if coordinates[1] != "distance":
        return print(f"Error: Invalid number of arguments. Usage python3 coordinate_system.py 'distance' '2,3,5' ")
    print(f"=== Game Coordinate System ===")
    pos0 = (0,0,0)      #x1 y1 z1
    print(f"Player Position Created {pos0}")
    try:
        raw_str = coordinates[2].split(',')
        new_pos = [int(num) for num in raw_str]
        if len(new_pos) != 3:
            raise CustomError("Error: Invalid amount of coordinates. Usage python3 coordinate_system.py '2,3,5'")
        print(f"Parsed Position {new_pos}")
        print(f"Distance between {pos0} and {new_pos} : {round(find_distance(pos0, new_pos),2)}")
        print()
    except (CustomError, IndexError, ValueError) as e:
        print(f"Error: {e}")
    print(f"=== Game Coordinate System Closing ===")
    return None






if __name__ == "__main__":
    coordinate_system(sys.argv[0:])
    pass