
import sys
from collections import defaultdict

def main():
    k, n1, n2, n3, t1, t2, t3 = map(int, sys.stdin.read().split())
    washers = [0] * n1
    dryers = [0] * n2
    folders = [0] * n3
    
    wash_queue = []
    dry_queue = []
    fold_queue = []
    
    for i in range(k):
        if washers[0] <= dryers[0] and washers[0] <= folders[0]:
            wash_time = washers[0]
            washers = [t1 + wash_time for t1 in washers]
            dry_queue.append((wash_time, i))
        elif dryers[0] <= washers[0] and dryers[0] <= folders[0]:
            dry_time = dryers[0]
            dryers = [t2 + dry_time for t2 in dryers]
            fold_queue.append((dry_time, i))
        else:
            fold_time = folders[0]
            folders = [t3 + fold_time for t3 in folders]
        
        if len(wash_queue) < n1:
            wash_queue.append((0, i))
        elif len(dry_queue) < n2:
            dry_queue.append((0, i))
        elif len(fold_queue) < n3:
            fold_queue.append((0, i))
        
    washers.sort()
    dryers.sort()
    folders.sort()
    
    print(max(washers[-1], dryers[-1], folders[-1]))


if __name__ == "__main__":
    main()

