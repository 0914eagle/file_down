
import sys
import heapq
def laundry(k, n_1, n_2, n_3, t_1, t_2, t_3):
    washers = [0] * n_1
    dryers = [0] * n_2
    folders = [0] * n_3
    wash_q = []
    dry_q = []
    fold_q = []
    for i in range(n_1):
        heapq.heappush(wash_q, (washers[i], i))
    for i in range(n_2):
        heapq.heappush(dry_q, (dryers[i], i))
    for i in range(n_3):
        heapq.heappush(fold_q, (folders[i], i))
    
    time = 0
    
    for _ in range(k):
        wash_t, wash_i = heapq.heappop(wash_q)
        dry_t, dry_i = heapq.heappop(dry_q)
        fold_t, fold_i = heapq.heappop(fold_q)
        
        time = max(wash_t, dry_t, fold_t)
        
        washers[wash_i] = time + t_1
        dryers[dry_i] = time + t_2
        folders[fold_i] = time + t_3
        
        heapq.heappush(wash_q, (washers[wash_i], wash_i))
        heapq.heappush(dry_q, (dryers[dry_i], dry_i))
        heapq.heappush(fold_q, (folders[fold_i], fold_i))
    
    return time
if __name__ == '__main__':
    k, n_1, n_2, n_3, t_1, t_2, t_3 = map(int, sys.stdin.read().split())
    print(laundry(k, n_1, n_2, n_3, t_1, t_2, t_3))

