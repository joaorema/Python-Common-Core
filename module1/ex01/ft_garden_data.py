class Plant:
    def __init__(self, name : str, height : int , age : int):
        self.name = name
        self.height = height
        self.age = age

def ft_garden_data():
    plant1 = Plant('Rose', 25, 30)
    plant2 = Plant("Sunflower", 80, 45)
    plant3 = Plant("Cactus", 15, 120)
    inventory = [plant1, plant2, plant3]
    for i in range(inventory.__len__()):
        print(inventory[i].name,":", inventory[i].height, "cm, ", inventory[i].age, "days old")

if __name__ == "__main__":
    ft_garden_data()