
def missing_gems():
    gems = {
        "power": "Power",
        "time": "Time",
        "space": "Space",
        "soul": "Soul",
        "reality": "Reality",
        "mind": "Mind"
    }

    seen_gems = set()
    n = int(input())
    for _ in range(n):
        color = input().strip()
        for key, value in gems.items():
            if color.lower() == key:
                seen_gems.add(value)

    missing_gems = set(gems.values()) - seen_gems
    print(len(missing_gems))
    for gem in missing_gems:
        print(gem)

missing_gems()
