import sys

class CustomError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def ancient_text(arg):
    print(f"=== Cyber Archives - Data Recovery System ===")
    print()
    print(f"Accessing Storage Vault: {arg}")
    try:
        text = open(arg, "r")
        print(f"Connection established")
        print(f"RECOVERED DATA:")
        print(text.read())
        text.close()
    except FileNotFoundError:
        print(f"ERROR: Storage vault not found")
    finally:
        print(f"Data recovery completed. Storage unit disconnected.")



if __name__ == "__main__":
    try:
        ancient_text(sys.argv[1])
    except (CustomError, IndexError) as e:
        print(f"Program usage: python3 ancient_text.py 'filename.txt'")