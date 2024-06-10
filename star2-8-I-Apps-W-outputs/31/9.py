
def equip_computers(n_usb, n_ps2, n_both, mouses):
    min_usb = min_ps2 = float('inf')
    for val, port in mouses:
        if port == 'USB' and val < min_usb:
            min_usb = val
        elif port == 'PS/2' and val < min_ps2:
            min_ps2 = val
    
    total_cost = min(min_usb, min_ps2)
    n_equipped = n_both + min(n_usb, n_ps2)
    if min_usb < min_ps2:
        n_equipped += n_usb
    else:
        n_equipped += n_ps2
    
    return n_equipped, total_cost


if __name__ == "__main__":
    n_usb, n_ps2, n_both = map(int, input().split())
    mouses = []
    for _ in range(int(input())):
        val, port = input().split()
        mouses.append((int(val), port))
    
    print(*equip_computers(n_usb, n_ps2, n_both, mouses))

