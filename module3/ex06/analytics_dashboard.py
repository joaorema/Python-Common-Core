import sys
import math
import random


class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__()
    def __str__(self):
        return self.message



def analytics_dashboard():
    player = [
        {"Name": "john", "score" : 2300, "achievements" : ["first_kill", "level_10", "first_blood"], "region": "north"},
        {"Name": "stacy", "score" : 5000, "achievements": ["boss_killer", "bomber"], "region": "east"},
        {"Name": "fernando", "score": 1000, "achievements": ["boss_killer", "level_10"], "region": "east"},
        {"Name": "greg", "score": 4200, "achievements": ["first_kill", "bomber"], "region": "central"},
    ]
    #List
    high_score = [p["Name"] for p in player if p["score"] > 2000]
    double_score = [p["score"]*2 for p in player]
    print(f"Testing List")
    print(f"High score: {high_score}")
    print(f"Double score: {double_score}")
    #Dict
    player_scores = {p["Name"]: p["score"] for p in player}
    achievement_count = {p["Name"]: len(p["achievements"]) for p in player}
    print(f"Testing dictionary")
    print(f"Player scores: {player_scores}")
    print(f"Achievement count: {achievement_count}")
    #Set
    print(f"Testing Sets")
    scores = [p["score"] for p in player]
    username = [p["Name"] for p in player]
    achievements = [ach for p in player for ach in p["achievements"]]
    unique = {ach for ach in achievements if achievements.count(ach) == 1}
    active_regions = {p["region"] for p in player}
    top_performer = [p["Name"] for p in player if p["score"] == max(scores)]
    top_performer_achievements = [p["achievements"] for p in player if p["Name"] == top_performer[0]]
    print(f"Unique Player: ", end=" ")
    for i in range(len(username)):
        print(f"'{username[i]}'", end=" ")
    print()
    print(f"Unique achievements: {unique}")
    print(f"Active regions: {active_regions}")

    print(f"=== Combined Analysis ===")
    print(f"Total Players: {len(player)}")
    print(f"Total unique achievements: {len(unique)}")
    print(f"Average Score: {sum(scores)/len(scores)}")
    print(f"Top performance: {top_performer} ({max(scores)} points, {len(top_performer_achievements)+1} achievements)")




if __name__ == "__main__":
    analytics_dashboard()