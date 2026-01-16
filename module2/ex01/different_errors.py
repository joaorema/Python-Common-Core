def cap(text:str):
    text.capitalize()

def garden_operations():
    try:
        print("===Test 1 ValueError===")
        x = int(input("Enter a name: "))
    except ValueError as e:
        print(f"Type Error: {e}")

    try:
        print("===Test 2 ZeroDivisionError===")
        print("Trying to divide 10 by 0")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Type Error: {e}")

    try:
        print("===Test 3 FileNotFoundError ===")
        print("Trying to open invalid file")
        open("coco.txt")
    except FileNotFoundError as e:
        print(f"File Error: {e}")

    try:
        print("===Test 4 KeyError===")
        print("Trying to print invalid key in dictionary")
        inventory = {"id" : "1" , "name": "joao"}
        print(inventory["email"])
    except KeyError as e:
        print(f"Key Error: {e}")

    try:
        print("===Test 5 Block with multiple executions Errors===")
        open("coco.txt")
    except(KeyError, TypeError, ZeroDivisionError, ValueError, FileNotFoundError) as e:
        print(f"Type Error: {e}")

    print("All error types tested successfully")

if __name__ == "__main__":
    garden_operations()
