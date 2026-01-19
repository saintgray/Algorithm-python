import sys
import math

"""
https://www.acmicpc.net/problem/1774
ref : Kruskal
"""
class V:
    n: int
    x: int
    y: int
    parent: None 

class E:
    v1: V
    v2: V
    d: int

def find(v):
   if v.parent == v:
       return v
   parent = find(v.parent)
   v.parent = parent
   return parent

def union(v1, v2):
    p1 = find(v1)
    p2 = find(v2)
    if p2.n < p2.n:
        p2.parent = p1
    else:
        p1.parent = p2
    
input = sys.stdin.readline
N, M = map(int, input().rstrip().split(' '))
vertex = [None for _ in range(N + 1)]
lines = []
for i in range(N):
    X, Y = map(int, input().rstrip().split(' '))
    v = V()
    v.n = i + 1
    v.x = X
    v.y = Y
    v.parent = v
    vertex[i + 1] = v
# 모든 간선 조합 생성
for i, v1 in enumerate(vertex[1:]):
   for j, v2 in enumerate(vertex[1:]):
       if v1 == v2:
           continue
       line = E()
       line.v1 = v1 
       line.v2 = v2
       line.d = (v1.x - v2.x)**2 + (v1.y - v2.y)**2 
       lines.append(line)
# 이미 존재하는 간선은 거리를 0으로 설정
for i in range(M):
    X, Y = map(int, input().rstrip().split(' '))
    v1 = vertex[X]
    v2 = vertex[Y]
    line = E()
    line.v1 = v1
    line.v2 = v2
    line.d = 0
    lines.append(line)
lines.sort(key= lambda line: line.d)

result = 0
for _, line in enumerate(lines):
    v1 = line.v1
    v2 = line.v2
    p1 = find(v1)
    p2 = find(v2)
    if p1 == p2:
        continue
    union(v1, v2)
    result += math.sqrt(line.d)
print(f'{round(result, 2):.2f}')