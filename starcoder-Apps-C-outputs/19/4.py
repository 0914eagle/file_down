
time_now = list(input())
time_final = list(input())
#print(time_final)
#print(time_now)
time_final[0],time_final[1],time_final[3],time_final[4] = time_now[0],time_now[1],time_now[3],time_now[4]

#print(time_final)

time_final = ''.join(time_final)
time_final = time_final.split(':')

time_final = int(time_final[0])*100 + int(time_final[1])

time_final = str(time_final)

time_final = time_final.rjust(4,'0')

#print(time_final)

#time_final = time_final.split(':')

#print(time_final)

#print(time_final)

#time_now = list(input())
#time_final = list(input())
#print(time_final)
#print(time_now)
time_now = ''.join(time_now)
time_now = time_now.split(':')

time_now = int(time_now[0])*100 + int(time_now[1])

time_now = str(time_now)

time_now = time_now.rjust(4,'0')

#print(time_now)

#time_now = time_now.split(':')

#print(time_now)

#print(time_final)

#print(time_now)

time_now = time_now.replace('0','9')
#print(time_now)

print(time_final)
print(time_now)
