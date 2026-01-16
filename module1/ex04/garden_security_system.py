plants = ["Rose", "Oak", "Cactus", "Sunflower", "Fern"]
starting_height = [15, 25, 28, 22, 10]
starting_age = [2, 16, 6, 14, 10]

class SecurePlant:
    def __init__(self, name, height,age):
        self.name = name
        if height <= 0:
            print("Invalid input for height!")
            return
        self.__height = height
        if age <= 0:
            print("Invalid input for age!")
            return
        self.__age = age


    def set_age(self, amount:int):
        if amount <= 0:
            return print("Invalid operation attempted: age", amount, "[REJECTED]")
        self.__age = amount
        return print("Age updated:", amount,"days [OK]")

    def set_height(self, amount:int):
        if amount <= 0:
            return print("Invalid operation attempted: height", amount, "[REJECTED]")

        self.__height = amount
        return print("Height updated:", amount,"cm" , "[OK]")

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def get_stats(self):
        return print("Current Plant:",self.name,"(",self.get_height(),"cm",self.get_age(),"days)" )


def garden_security_system():
    inventory = []
    for i in range(5):
        new_plant = SecurePlant(plants[i], starting_height[i], starting_age[i])
        inventory.append(new_plant)

    print("=== Garden Security System ===")
    print("Plant created:", inventory[0].name)
    inventory[0].set_height(25)
    inventory[0].set_age(30)
    inventory[0].set_height(-5)
    inventory[0].set_age(0)

    inventory[0].get_stats()




if __name__ == "__main__":
    garden_security_system()