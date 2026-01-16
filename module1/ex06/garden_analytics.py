class Plant:
    def __init__(self, name: str,height: int, age: int):
        self.name = name
        self.height = height
        self.age = age
        self.type = "regular"
    def get_stats(self):
        return f"{self.name}: {self.height}cm"

class FloweringPlant(Plant):
    def __init__(self, name: str, height: int, age: int, color:str):
        super().__init__(name,height,age)
        self.color = color
        self.type = "flowering"
    def get_stats(self):
        return f"{self.name}: {self.height}cm, {self.color} flowers (blooming)"

class PrizeFlower(FloweringPlant):
    def __init__(self, name: str, height: int, age: int, color: str, point: int):
        super().__init__(name,height,age, color)
        self.point = point
        self.type = "prize flowers"
    def get_stats(self):
        return f"{super().get_stats()}, Prize points: {self.point}"

class Garden:
    def __init__(self, name: str):
        self.name = name
        self.plants = []
        self.plants_amount = 0
        self.garden_growth = 0

    def get_username(self):
        return self.name

    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.name}'s garden")
        self.plants_amount += 1

    def get_growth(self):
        return self.garden_growth


class GardenManager:

    class GardenStats:
        #GardenStats Class
        @staticmethod
        def calculate_height(garden):
            return sum(x.height for x in garden.plants)
        @staticmethod
        def validate_height(garden):
            for x in garden.plants:
                if x.height < 0:
                    return False
            return True
        @staticmethod
        def grow_garden(garden, amount):
            print(f"{garden.get_username()} is helping all plants grow...")
            for x in garden.plants:
                x.height += amount
                garden.garden_growth += amount
                print(f"{x.name} grew {amount}cm")
        @staticmethod
        def garden_info(garden):
            print("Plants in garden :")
            for x in garden.plants:
                print(x.get_stats())
            print(f"Plants added: {garden.plants_amount}, grow: {garden.get_growth()}cm")
            regular = 0
            flowering = 0
            prize_flower = 0
            for x in garden.plants:
                if x.type == "regular":
                    regular += 1
                elif x.type == "flowering":
                    flowering += 1
                else:
                    prize_flower += 1
            print(f"Plant types: {regular} regular, {flowering} flowering, {prize_flower} prize flowers")
            is_valid = GardenManager.GardenStats.validate_height(garden)
            print(f"Height validation test: {is_valid}")
        @staticmethod
        def get_garden_score(garden):
            y = 0
            for x in garden.plants:
                y += x.height
            return y

    #Game Manager
    def __init__(self, owner_name:str):
        self.owner_name = owner_name
        self.gardens = {}  #dict for gardens


    def create_garden(self, garden_name):
        new_garden = Garden(garden_name)
        self.gardens[garden_name] = new_garden      # "Name" : Garden Object
        return new_garden

    def gardens_amount(self):
        return len(self.gardens)

    def print_gardens(self ):
        print(self.gardens)


    @classmethod
    def create_garden_network(cls):
        print("Starting global garden network")
        return cls("Networkd admin")



if __name__ == "__main__":
    #create manager
    gm = GardenManager.create_garden_network()
    #add new garden to manager
    my_garden = gm.create_garden("João")
    her_garden = gm.create_garden("Ana")

    #add new plants for Joao garden
    my_garden.add_plant(Plant("Oak Tree", 101, 25))
    my_garden.add_plant(FloweringPlant("Rose", 26, 15, "red"))
    my_garden.add_plant(PrizeFlower("Sunflower", 6, 15, "yellow", 42))
    #add new plants to Ana garden
    her_garden.add_plant(Plant("Oak Tree", 55, 25))
    her_garden.add_plant(FloweringPlant("Lily", 15, 15, "yellow"))
    her_garden.add_plant(PrizeFlower("Sunflower", 12, 15, "yellow", 42))
    her_garden.add_plant(PrizeFlower("Mega Rose", 22, 15, "red", 84))


    #grow
    GardenManager.GardenStats.grow_garden(my_garden, 2)
    GardenManager.GardenStats.garden_info(my_garden)
    GardenManager.GardenStats.grow_garden(her_garden, 5)
    GardenManager.GardenStats.garden_info(her_garden)
    print(f"Total gardens managed: {gm.gardens_amount()}")
    print(f"Garden Score:{my_garden.name} {GardenManager.GardenStats.get_garden_score(my_garden)}, {her_garden.name} {GardenManager.GardenStats.get_garden_score(her_garden)}" )

    gm.print_gardens()





