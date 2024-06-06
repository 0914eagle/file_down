
import sys
def getints():
    return map(int, raw_input().split())

n, h, m, k = getints()
trains = map(int, raw_input().split())
trains.sort()

def test(t, trains):
    #print 't', t
    in_service = 0
    for train in trains:
        if train < t:
            in_service += 1
        elif train + k > t + m/2:
            break
    #print 'in_service', in_service
    return in_service

def test_opt(t, trains):
    in_service = test(t, trains)
    if t > 0:
        in_service = max(in_service, test(t - 1, trains))
    if t < m/2:
        in_service = max(in_service, test(t + 1, trains))
    return in_service

opt_in_service = -1
opt_t = None
for t in xrange(m/2 + 1):
    in_service = test_opt(t, trains)
    #print 't', t, 'in_service', in_service
    if in_service > opt_in_service:
        opt_in_service = in_service
        opt_t = t

print m/2 - opt_in_service, opt_t
for t in xrange(m/2 + 1):
    if test_opt(t, trains) < opt_in_service:
        print t + 1,
