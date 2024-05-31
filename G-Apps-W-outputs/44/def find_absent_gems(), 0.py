
def find_absent_gems():
    gems = {'purple': 'Power', 'green': 'Time', 'blue': 'Space', 'orange': 'Soul', 'red': 'Reality', 'yellow': 'Mind'}
    
    n = int(input())
    present_gems = set()
    
    for _ in range(n):
        color = input()
        gem_name = gems[color]
        present_gems.add(gem_name)
    
    all_gems = ['Power', 'Time', 'Space', 'Soul', 'Reality', 'Mind']
    absent_gems = [gem for gem in all_gems if gem not in present_gems]
    
    print(len(absent_gems))
    for gem in absent_gems:
        print(gem)

find_absent_gems()
