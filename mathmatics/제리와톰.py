import sys

input=sys.stdin.readline
N, M=map(int, input().rstrip().split(' '))
print('{} {}'.format(M-N, M))

