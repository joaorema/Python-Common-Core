plants = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
starting_height = [15, 25, 28, 22, 10]
starting_age = [2, 16, 6, 14, 10]
increment_height = [1, 3, 2, 2, 3, 1]

class Plant:
    def __init__(self, name, init_height, init_age):
        self.name = name
        self.height = init_height
        self.age = init_age


def plant_factory():
    inventory = []
    for i in range(5):
        new_plant = Plant(plants[i], starting_age[i], starting_age[i])
        print("Created:", new_plant.name,"(", starting_age[i],"cm ,", new_plant.age,"days)")
        inventory.append(new_plant)
    print("Total plants created: ", len(inventory))


if __name__ == "__main__":
    plant_factory()