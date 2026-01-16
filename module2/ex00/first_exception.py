#int() print()

def check_temperature(temp_str):
    try:
        value = float(temp_str)
        if value > 40:
            print(f"Error: {value}ºC is too hot for plants (max 40ºC)")
            return None
        elif value < 0:
            print(f"Error: {value}ºC is too cold for plants (min 0ºC)")
            return None
        else:
            print(f"Valid temperature: {value}ºC")
            return value
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number.")
        return None

def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    tests = ["25", "abc", "100", "-25"]
    for test in tests:
        check_temperature(test)



    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    temp = input("Temperature: ")
    check_temperature(temp)
    test_temperature_input()

