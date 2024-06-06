
def p_f_s(list1,list2):
    list1_ = list1.copy()
    for i in range(len(list2)):
        if list2[i] not in list1:
            return "Impossible"
        if list2[i] in list1:
            list1_.remove(list2[i])
    list1_.sort()
    return "Possible\n"+" ".join(map(str,list1_+list2))

if __name__=="__main__":
    n,m=map(int,input().strip().split())
    list1=list(map(int,input().strip().split()))
    list2=list(map(int,input().strip().split()))
    print(p_f_s(list1,list2))
