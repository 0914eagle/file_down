
#Data center ,day length of day,number of clients
n,m,h = map(int,input().split())

#maintenance time
maintenance_time = list(map(int,input().split()))

#list of clients data center
client_data_center = []

#list of clients data center
for i in range(m):
    client_data_center.append(list(map(int,input().split())))

#2 way replication
for i in range(len(client_data_center)):
    if maintenance_time[client_data_center[i][0]] == maintenance_time[client_data_center[i][1]]:
        print(1)
        print(client_data_center[i][0])
        break
    elif maintenance_time[client_data_center[i][0]]+1 == maintenance_time[client_data_center[i][1]]:
        print(1)
        print(client_data_center[i][1])
        break
    elif maintenance_time[client_data_center[i][0]]-1 == maintenance_time[client_data_center[i][1]]:
        print(1)
        print(client_data_center[i][0])
        break
    elif maintenance_time[client_data_center[i][0]] == maintenance_time[client_data_center[i][1]]-1:
        print(1)
        print(client_data_center[i][1])
        break
    else:
        continue
