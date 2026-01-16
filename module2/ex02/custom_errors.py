class GardenError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}"

class PlantError(GardenError):
    pass

class WaterError(GardenError):
    pass

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return f"{self.message}"

class TempError(CustomError):
    pass


def temp_check(value):
    if value < 0:
        raise TempError("The temperature can not be negative")
    elif value > 100:
        raise TempError("The temperature can not be greater than 100")
    else:
        print(f"Perfect temperature")


def water_plant(liters):
    if liters < 0:
        raise WaterError("Not enough water in the tank")

def plant(name):
    if len(name) > 0:
        raise GardenError("the tomato plant is wilting")


if __name__ == "__main__":
    try:
        water_plant(-1)
    except (GardenError, WaterError, PlantError) as e:
        print(F"Error Type :{e}")

    try:
        plant("teste")
    except (GardenError, WaterError, PlantError) as e:
        print(F"Error Type :{e}")

    try:
        water_plant(2)
        plant("teste")
    except GardenError as e:
        print(F"Error Type :{e}")

    try:
        temp_check(200)
    except CustomError as e:
        print(F"Error Type :{e}")