
import sys

def get_dice_probabilities(a, b):
    probabilities = {}
    for i in range(a, b + 1):
        for j in range(a, b + 1):
            probabilities[i + j] = probabilities.get(i + j, 0) + 1
    return probabilities

def get_dice_probabilities_sorted(a, b):
    probabilities = get_dice_probabilities(a, b)
    return sorted(probabilities.items(), key=lambda x: x[0])

def get_dice_probabilities_sorted_reversed(a, b):
    probabilities = get_dice_probabilities(a, b)
    return sorted(probabilities.items(), key=lambda x: x[0], reverse=True)

def get_probability_of_winning(gunnar_dice, emma_dice):
    gunnar_probabilities = get_dice_probabilities_sorted(gunnar_dice[0], gunnar_dice[1])
    emma_probabilities = get_dice_probabilities_sorted_reversed(emma_dice[0], emma_dice[1])
    gunnar_wins = 0
    for gunnar_probability in gunnar_probabilities:
        for emma_probability in emma_probabilities:
            if gunnar_probability[0] > emma_probability[0]:
                gunnar_wins += gunnar_probability[1] * emma_probability[1]
            elif gunnar_probability[0] == emma_probability[0]:
                return "Tie"
    return gunnar_wins / (gunnar_dice[1] - gunnar_dice[0] + 1) ** 2

def main():
    gunnar_dice = list(map(int, sys.stdin.readline().split()))
    emma_dice = list(map(int, sys.stdin.readline().split()))
    probability = get_probability_of_winning(gunnar_dice, emma_dice)
    if probability > 0.5:
        print("Gunnar")
    elif probability < 0.5:
        print("Emma")
    else:
        print("Tie")

if __name__ == "__main__":
    main()

