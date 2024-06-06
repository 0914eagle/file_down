
import sys
n,p=map(float,input().split())
energy=[0]*int(n)
prob=[0]*int(n)
for i in range(int(n)):
    energy[i],prob[i]=map(float,sys.stdin.readline().split())
energy.sort()
prob.sort()
energy.reverse()
prob.reverse()
#print(energy)
#print(prob)
total=0
for i in range(int(n)):
    if(p<prob[i]):
        total+=energy[i]
        p=(1-p)*prob[i]+p
print(int(total))
