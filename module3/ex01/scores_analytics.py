import sys

class CustomError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)
    def __str__(self):
        return self.message


def score_analytics(player_scores):
    print(f"=== Player Score Analytics ===")
    if len(player_scores) == 1:
        return print(f"No scores provided!. Usage: python3 scores_analytics.py <score1> <score2>")
    else:
        try:
            new_list =[]
            for i in range(1,len(player_scores)):
                new_list.append(float(player_scores[i]))
            print(f"Scores processed: {player_scores[1:]}")
            print(f"Total Players: {len(player_scores) -1}")
            total_score = sum(new_list)
            player_amount = float(len(player_scores))
            average_score = total_score / player_amount
            print(f"Total Score: {int(total_score)}")
            print(f"Average Score: {round(average_score,2)}")
            print(f"High Score: {int(max(new_list))}")
            print(f"Low Score: {int(min(new_list))}")

        except (CustomError, IndexError, ValueError) as e:
            print(e)
        finally:
            pass


if __name__ == "__main__":
    score_analytics(sys.argv[0:])
    pass