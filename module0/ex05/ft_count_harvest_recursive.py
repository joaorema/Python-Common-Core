#expects input from user that sets total days that starts null
#current day set to 1 to go from 1 to total days
def count_harvest_recursive(total_days=None, current_day=1):
    if total_days is None:
        total_days = int(input("Days until harvest: "))

    if current_day > total_days:
        print("Harvest time!")
        return

    print(f"Days: {current_day}")

    count_harvest_recursive(total_days, current_day + 1)

count_harvest_recursive()