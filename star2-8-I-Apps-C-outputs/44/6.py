
def solve(H, W, web_page):
    web_page = [[c for c in line] for line in web_page]
    
    def check_ad(x, y):
        if x < 0 or x >= H or y < 0 or y >= W:
            return False
        if web_page[x][y] == "+":
            return True
        
        allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!., ")
        if web_page[x][y] not in allowed_chars:
            return True
        
        return False
    
    def check_inside_ad(x, y):
        if x < 0 or x >= H or y < 0 or y >= W:
            return False
        if web_page[x][y] == "+":
            return True
        
        allowed_chars = set("0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ?!., ")
        if web_page[x][y] not in allowed_chars:
            return False
        
        return True
    
    def find_ad_size(x, y):
        q = [(x, y)]
        size = 0
        while len(q) > 0:
            x, y = q.pop(0)
            if check_ad(x, y):
                size += 1
                q += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        return size
    
    def remove_ad(x, y):
        q = [(x, y)]
        while len(q) > 0:
            x, y = q.pop(0)
            if check_inside_ad(x, y):
                web_page[x][y] = " "
                q += [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    
    for x in range(H):
        for y in range(W):
            if check_ad(x, y):
                size = find_ad_size(x, y)
                remove_ad(x, y)
    
    web_page = ["".join(line) for line in web_page]
    
    return web_page

