from traceback import print_tb
from unicodedata import name


from collections import Counter

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return self.message


def achievement_tracker():
    print(f"Achievement Tracker")
    print()
    alice = {"first_kill", "level_10", "treasure_hunter", "speed_demon"}
    bob = {"first_kill", "level_10", "boss_slayer", "collector"}
    charlie = {"level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"}
    print(f"Player Alice Achievements: {alice}")
    print(f"Player Bob Achievements: {bob}")
    print(f"Player Charlie Achievements: {charlie}")
    #union returns all unique achievements from the 3 Players
    new_set = alice.union(bob.union(charlie))
    #intersection returns the most common from the 3 Players
    common = alice.intersection(bob.intersection(charlie))
    #rarest
    all_ach = alice | bob | charlie
    shared_ab = alice & bob
    shared_bc = bob & charlie
    shared_ac = alice & charlie
    all_shared = shared_ab | shared_bc | shared_ac
    rare = all_ach - all_shared
    alice_unique = (alice - bob) - (alice - charlie)
    bob_unique = (bob - charlie) - (bob - alice)
    charlie_unique = (charlie - alice) - (charlie - bob)


    print(f"=== Achievement Analytics ===")
    try:
        print(f"All unique achievements: {new_set}")
        print(f"Total unique achievements: {len(new_set)}")
        print(f"Common to all players : {common}")
        print(f"Rare Achievements (1 Player): {rare}")
        print()
        print(f"Alice and Bob common: {shared_ab}")
        print(f"Alice unique: {alice_unique}")
        print(f"Bob unique: {bob_unique}")
        print(f"Charlie unique: {charlie_unique}")




    except (CustomError, ImportError, SystemError) as e:
        print(e)

if __name__ == "__main__":
    achievement_tracker()