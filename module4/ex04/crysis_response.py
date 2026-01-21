#open read write print
import sys


def crisis_response():
    print(f"=== Cyber ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    try:
        print(f"CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            print(file.read())
            print(f"STATUS: Normal operation resumed")
    except FileNotFoundError:
        print(f"RESPONSE: Archive not found in storage matrix")
        print(f"STATUS: Crisis handled, security maintained")
    finally:
        print()

    try:
        print(f"CRISIS ALERT: Attempting access to 'classified_data.txt'...")
        with open("classified_data.txt", "r") as file:
            print(file.read())
    except PermissionError as error:
        print(f"[RESPONSE]: Security protocol deny access")
        print(f"STATUS: Crisis handled, security maintained")
    finally:
        print()

    try:
        print(f"ROUTINE ACCESS: Attempting access to 'standard_archive.txt'...")
        with open("standard_archive.txt", "r") as file:
            print(f"[SUCCESS]: Archive recovered - {file.read()}")
            print(f"STATUS: Normal operation resumed")
    except (PermissionError,FileExistsError, FileNotFoundError) as error:
        print(f"[RESPONSE]: {error}")
        print(f"STATUS: Crisis handled, security maintained")
    finally:
        print()

    print(f"All crisis scenarios handled successfully. Archive secure.")

if __name__ == "__main__":
    crisis_response()

