from collections import Counter

def ucl_final(n, goals):
    if n == 1:
        return goals[0]
    
    goal_counts = Counter(goals)
    max_goals = max(goal_counts.values())
    
    winners = [team for team, count in goal_counts.items() if count == max_goals]
    
    if len(winners) > 1:
        for goal in reversed(goals):
            if goal in winners:
                return goal
    else:
        return winners[0]

if __name__ == "__main__":
    n = int(input())
    goals = [input().strip() for _ in range(n)]
    print(ucl_final(n, goals))