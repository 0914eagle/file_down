
import sys

#input
n_r,n_c,n,m = input().split()
n_r,n_c,n,m = int(n_r),int(n_c),int(n),int(m)

icons = []

for i in range(n+m):
    r,c = input().split()
    r,c = int(r),int(c)
    icons.append((r,c))

def delete(icon_to_delete,icons):
    icons_to_delete = []
    for i in icons:
        if i[0] <= icon_to_delete[0]+15 and i[0]+15 >= icon_to_delete[0] and i[1] <= icon_to_delete[1]+9 and i[1]+9 >= icon_to_delete[1]:
            icons_to_delete.append(i)
    for i in icons_to_delete:
        icons.remove(i)
    return icons

icons = delete(icons[0],icons)
print(len(icons))
