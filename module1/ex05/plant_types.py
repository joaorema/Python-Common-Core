class Plant:
    def __init__(self, name:str, height:int, age:int):
        self.name = name
        self.height = height
        self.age = age

class Flower(Plant):
    def __init__(self, name:str, height:int, age:int, color:str):
        super().__init__(name,height, age)
        self.color = color

    def bloom(self):
        return print(self.name, "is blooming beautifully!")

    def present(self):
        return print(self.name, "(Flower):", self.height,"cm,", self.age,"days,", self.color, "color")

class Tree(Plant):
    def __init__(self, name:str, height:int, age:int, diameter:int):
        super().__init__(name,height,age)
        self.diameter = diameter

    def shade(self):
        print(self.name, "provides", self.diameter + 28, "square meters of shade" )
        pass

    def present(self):
        return print(self.name, "(Tree):", self.height,"cm,", self.age,"days,", self.diameter, "cm")

class Vegetable(Plant):
    def __init__(self, name:str, height:int, age:int, season: str):
        super().__init__(name,height,age)
        self.season = season

    def nutrition_value(self):
        print(self.name, "is rich in vitamin C")

    def present(self):
        return print(self.name, "(Vegetable):", self.height,"cm,", self.age,"days,", self.season, "harvest")





def plant_types():
    print("=== Garden Plant Types ===")
    flower = Flower("Rose", 20, 30, "red")
    flower.present()
    flower.bloom()

    tree = Tree("Oak", 500, 1825, 50)
    tree.present()
    tree.shade()

    vegetable = Vegetable("Tomato", 80, 90, "summer")
    vegetable.present()
    vegetable.nutrition_value()


if __name__ == "__main__":
    plant_types()