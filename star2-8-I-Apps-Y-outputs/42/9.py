
import sys
votes = sys.stdin.read().splitlines()
votes = votes[:-1]
candidate_dict = {}
for vote in votes:
    if vote not in candidate_dict:
        candidate_dict[vote] = 1
    else:
        candidate_dict[vote] += 1
majority = max(candidate_dict.values())
if majority > len(votes)/2:
    print(max(candidate_dict, key=candidate_dict.get))
else:
    print("Runoff!")

