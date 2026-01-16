def ft_plant_age():
    time = int(input("Enter plant age in days: "))
    if time > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")

ft_plant_age()