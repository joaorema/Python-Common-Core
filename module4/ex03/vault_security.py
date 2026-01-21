#open read write print
import sys

def vault_security(arg):
    print(f"=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    try:
        print(f"Initializing secure vault access...")
        with open(arg) as file:
            print(f"Vault connection established with failsafe protocols")
            print()
            print(f"SECURE EXTRACTION")
            print(file.read())
            print()

    except (FileNotFoundError, FileExistsError, PermissionError) as err:
        sys.stderr.write(f"[ERROR] {err}\n")

    try:
        print(f"Appending security protocols to vault...")
        with open(arg, "a") as file:
            file.write(f"[CLASSIFIED] New security protocols archived\n")
            print(f"Successfully added security protocols to vault.")
    except (FileNotFoundError, FileExistsError, IndexError, PermissionError) as error:
        sys.stderr.write(f"[ERROR] {error}\n")

    print()
    print(f"SECURE PRESERVATION")
    print(f"[CLASSIFIED] New security protocols archived")
    print(f"Vault automatically sealed upon completion")
    print()
    print(f"All vault operations completed with maximum security.")

if __name__ == "__main__":
    try:
        vault_security(sys.argv[1])
    except (FileNotFoundError, FileExistsError, IndexError) as e:
        print(f"[ERROR] Program usage: python3 vault_security.py 'filename'")