class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message

class Plant:
    def __init__(self, name, water_amount, sun_amount):
        self.name = name
        self.water_amount = water_amount
        self.sun_amount = sun_amount
    def get_name(self):
        return self.name
    def get_water_amount(self):
        return self.water_amount
    def get_sun_amount(self):
        return self.sun_amount

class Garden:
    def __init__(self, name):
        self.name = name
        self.plants = []

    def add_plant(self, plant):
        if len(plant.get_name()) == 0:
            raise CustomException("Plant name cannot be empty")
        self.plants.append(plant)
        print(f"Added {plant.get_name()} successfully")

class GardenManager:
    class PlantControl:
        @staticmethod
        def water_plants(garden, water_amount):
            print(f"===Opening watering system===")
            try:
                for plant in garden.plants:
                    if plant.get_water_amount() + water_amount > 25:
                        raise CustomException(f"{plant.get_name()} has too much water.")
                    print(f"Watering {plant.get_name()} - Success")
            except CustomException as e:
                print(e)
            finally:
                print("===Closing watering system===")
        @staticmethod
        def get_health(garden):
            try:
                for plant in garden.plants:
                    if 1 < plant.get_water_amount() > 10:
                        raise CustomException(f"{plant.get_name()} has wrong water level.")
                    elif 2 < plant.get_sun_amount() > 12:
                        raise CustomException(f"{plant.get_name()} has wrong sun level.")
                    print(f"{plant.get_name()}: healthy (water:{plant.get_water_amount()},sun:{plant.get_sun_amount()})")
            except CustomException as e:
                print(e)
            finally:
                pass

    def __init__(self,name):
        self.name = name
        self.gardens = {}

    def add_garden(self, name):
        new_garden = Garden(name)
        self.gardens[name] = new_garden
        return new_garden

def test_garden_management():
    print(f"=== Garden Management System ===")
    gm = GardenManager("Tom")
    garden1 = gm.add_garden("Tom")
    try:
        print(f"Adding plants to garden")
        garden1.add_plant(Plant("Tomato", 5, 8))
        garden1.add_plant(Plant("Lettuce", 15, 8))
        garden1.add_plant(Plant("", 5, 8))
    except CustomException as e:
        print(e)
    finally:
        print("No longer adding plants")
    print("-" * 30)
    gm.PlantControl.water_plants(garden1, 10)
    print("-" * 30)
    gm.PlantControl.get_health(garden1)
    print("-" * 30)
    print(f"Testing Error Recovery")
    print(f"System Recovering and continuing")
    print(f"Guard Management test complete!")

if __name__ == "__main__":
    test_garden_management()


