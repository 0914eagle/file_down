
from collections import defaultdict
import sys
votes = defaultdict(int)
for line in sys.stdin:
    if line.strip() == '***':
        break
    votes[line.strip()] += 1
sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)
if sorted_votes[0][1] > sorted_votes[1][1]:
    print(sorted_votes[0][0])
else:
    print('Runoff!')

