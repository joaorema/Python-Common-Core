import sys


def archive_creation():
    print(f"=== Cyber Archives - Preservation System ===")
    print(f"Initializing new storage unit : new_discovery_text")
    try:
        file = open("new_discovery_text.txt", "x")
        print(f"Storage unit created successfully")
        print(f"Inscribing preservation data...")
        file.write(f"[ENTRY 001] New quantum algorithm discovered\n")
        file.write(f"[ENTRY 002] Efficiency increased by 34%\n")
        file.write(f"[ENTRY 003] Archived by Data archivist trainee\n")

        print()
        print(f"[ENTRY 001] New quantum algorithm discovered")
        print(f"[ENTRY 002] Efficiency increased by 34%")
        print(f"[ENTRY 003] Archived by Data archivist trainee\n")
        print(f"Data inscription complete. Stora unit sealed")
        file.close()
        print(f"Archive 'new_discovery_text.txt' ready for long-term preservation")


    except (ImportError, FileNotFoundError, FileExistsError) as e:
        print(f"Storage failed to start: {e}")


if __name__ == "__main__":
    archive_creation()
    pass