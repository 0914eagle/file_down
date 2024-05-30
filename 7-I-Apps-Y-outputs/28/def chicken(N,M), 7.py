
def chicken(N,M):
    if N%M==0:
        return "Dr. Chaz will have {} piece[s] of chicken left over!".format(N-M)
    else:
        return "Dr. Chaz needs {} more piece[s] of chicken!".format(M-N%M)

