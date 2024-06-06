
class Message:
    def __init__(self, t, n):
        self.t = t
        self.n = n

n = int(input())
message_list = []
for i in range(n):
    t, c = map(int, input().split())
    message_list.append(Message(t, c))

q = 0
max_q = 0
last = 0

for m in message_list:
    if m.t > last:
        q += m.n
    else:
        q += m.n - (last - m.t + 1)
    max_q = max(max_q, q)
    last = m.t + m.n - 1

print(last, max_q)
