import sys
from queue import Queue
"""
https://www.acmicpc.net/problem/2211
ref : Dijkstra
"""
class V:
    n: int
    lans: None
    net_time: int # fastest network time above super computer
    prev_com: None

    def __init__(self, n):
        self.n = n
        self.lans = []
        self.net_time = -1
        self.prev_com = None

class Lan:
    to: V
    net_time: int

    def __init__(self, to, net_time):
        self.to = to
        self.net_time = net_time 

super_com = None
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(' '))
coms = [V(i + 1) for i in range(N)]
coms.insert(0, None)
super_com = coms[1]
super_com.net_time = 0
for i in range(M):
    A, B, C = map(int, input().rstrip().split(' '))
    coms[A].lans.append(Lan(coms[B], C))
    coms[B].lans.append(Lan(coms[A], C))

q = Queue()
q.put(super_com)
while not q.empty():
    com = q.get()
    for _, lan in enumerate(com.lans):
        _com = lan.to
        if _com.net_time == -1 or _com.net_time > com.net_time + lan.net_time:
            _com.net_time = com.net_time + lan.net_time
            _com.prev_com = com.n 
            q.put(_com)

count = 0
connections = []
for _, com in enumerate(coms[1:]):
    if com.prev_com is not None:
        count += 1
        connections.append(str(f'{com.n} {com.prev_com}'))
print(count)
for _, conn in enumerate(connections):
    print(conn)
