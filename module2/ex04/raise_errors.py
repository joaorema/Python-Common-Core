class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return self.message

def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        if len(plant_name) == 0:
            raise CustomError("Error: Plant Name cannot be empty")
        elif 1 < water_level > 10:
            raise CustomError("Error: Water Level must be between 1 and 10")
        elif 2 < sunlight_hours > 12:
            raise CustomError("Sunlight hours must be between 1 and 12")
        else:
            print(f"Plant '{plant_name}' is healthy ")
    except CustomError as e:
        print(e)

def test_plant_check():
    try:
        print(f"=== Garden Plant Health Checker ===")
        print(f"Testing Good Values")
        check_plant_health("Tomato", 5, 6)
        print("-" * 30)
        print(f"Testing empty plant name")
        check_plant_health("", 5, 6)
        print("-" * 30)
        print(f"Testing bad water levels")
        check_plant_health("Tomato", 15, 6)
        print("-" * 30)
        print(f"Testing bad sunlight hours")
        check_plant_health("Tomato", 5, 0)
        print("-" * 30)
    except CustomError as e:
        print(e)
    finally:
        print(f"All tests completed")


if __name__ == "__main__":
    test_plant_check()


