def solution(cards1, cards2, goal):
    for goal_word in goal:
        if len(cards1) != 0 and goal_word == cards1[0]:
            del cards1[0]
        elif len(cards2) != 0 and goal_word == cards2[0]:
            del cards2[0]
        else: return "No"
    return "Yes"
