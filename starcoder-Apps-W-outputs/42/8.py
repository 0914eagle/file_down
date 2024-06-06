
# BFS
class Solution:
    def find_min_max(self, points):
        x = []
        y = []
        z = []
        for i in points:
            x.append(i[0])
            y.append(i[1])
            z.append(i[2])
        return min(x), max(x), min(y), max(y), min(z), max(z)
    
    def is_in_box(self, point, box):
        return box[0] <= point[0] <= box[1] and box[2] <= point[1] <= box[3] and box[4] <= point[2] <= box[5]
    
    def find_two_points(self, points):
        from collections import defaultdict
        queue = defaultdict(list)
        visited = set()
        
        min_x, max_x, min_y, max_y, min_z, max_z = self.find_min_max(points)
        visited.add((min_x, max_x, min_y, max_y, min_z, max_z))
        queue[(min_x, max_x, min_y, max_y, min_z, max_z)] = 0
        
        while queue:
            key, level = queue.popitem()
            min_x, max_x, min_y, max_y, min_z, max_z = key
            if level == len(points)//2:
                return True
            for idx, p in enumerate(points):
                if idx in visited:
                    continue
                box = (min(key[0], p[0]), max(key[1], p[0]), min(key[2], p[1]), max(key[3], p[1]), min(key[4], p[2]), max(key[5], p[2]))
                if all([self.is_in_box(p, box) for p in points if p not in visited]):
                    if box not in visited:
                        visited.add(box)
                        queue[box] = level + 1
        return False
