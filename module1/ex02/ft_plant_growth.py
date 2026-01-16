class Plant:
    def __init__(self, name : str, height : int ,current_height : int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.current_height = height


    def grow(self, amount : int):
        self.current_height += amount

    def pass_time(self, amount : int):
        self.age += amount

    def get_info(self):
        print(self.name,": ", self.current_height,"cm, ", self.age, "days old")


def ft_garden_growth():
    plant1 = Plant('Rose', 25,25 ,30)
    plant2 = Plant("Sunflower", 80, 80,45)
    plant3 = Plant("Cactus", 15, 15,120)
    inventory = [plant1, plant2, plant3]
    for i in range(7):
        print("=== Day ", i + 1, "===")
        for x in range(3):
            if inventory[x].name == "Rose":
                inventory[x].grow(1)
            elif inventory[x].name == "Sunflower":
                inventory[x].grow(5)
            else:
                inventory[x].grow(3)
            inventory[x].pass_time(1)
            inventory[x].get_info()
            if i == 6:
                print("Growth this week: +", inventory[x].current_height - inventory[x].height, "cm")



if __name__ == "__main__":
    ft_garden_growth()