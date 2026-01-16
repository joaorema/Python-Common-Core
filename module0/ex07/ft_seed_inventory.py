def ft_seed_inventory(vegetable, amount, container):
    if container == "packets":
        print( vegetable.capitalize(),"seeds:", amount , container, "available")
    elif container == "grams":
        print( vegetable.capitalize(),"seeds:", amount, container, "total")
    elif container == "area":
        print(vegetable.capitalize(), "seeds: covers", amount, "square meters")
    else:
        print("Unknown unit type")


ft_seed_inventory("tomato", 15, "packets")
ft_seed_inventory("carrot", 8, "grams")
ft_seed_inventory("lettuce", 12, "area")
ft_seed_inventory("pilas", 5, "area")
ft_seed_inventory("piccolos", 42, "cao")