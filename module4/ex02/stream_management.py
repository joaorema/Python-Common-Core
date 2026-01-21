import sys
import selectors

def stream_management():
    sel = selectors.DefaultSelector()
    sys.stdout.write(f"=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()

    while True:
        text = input("Input stream active. Enter archivist ID: ")
        try:
            id_val = int(text)
            if id_val:
                break
        except (ValueError, TypeError)as e:
            sys.stdout.write(f"[ALERT] Invalid input for id use a number\n")
    message = input(f"Input stream active. Enter status report: ")
    print()
    sys.stdout.write(f"[STANDARD] Archive status from id {id_val}: {message}\n")
    sys.stderr.write(f"[ALERT] System diagnostics: Communication channel verified\n")
    sys.stdout.write(f"[STANDARD] Data transmission complete\n")
    print()
    sys.stdout.write(f"Three channel communication test successful\n")

if __name__ == "__main__":
    stream_management()