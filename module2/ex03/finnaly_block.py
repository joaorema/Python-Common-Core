class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message

def check_name(name):
    fruits = ["banana", "apple", "strawberry", "coconut" , "kiwi"]
    if name not in fruits:
        raise CustomError(f"{name} not a valid fruit!")

def watering_plants(plant_list):
    print(f"===Opening Watering System===")
    try:
        for plant in plant_list:
            check_name(plant)
            print(f"Watering {plant}")
    except CustomError as e:
        print(f"Error type: {e}")
    finally:
        print("===Closing Watering System===")

def test_watering_system():
    list1 = ["banana", "apple", "strawberry", "coconut", "kiwi"]
    list2 = ["apple", "strawberry", "Mango", "kiwi"]

    try:
        watering_plants(list1)
        watering_plants(list2)
    except CustomError as e:
        print(f"Error type: {e}")
    finally:
        print("Cleanup always happens!")


if __name__ == "__main__":
    test_watering_system()