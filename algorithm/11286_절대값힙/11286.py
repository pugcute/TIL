import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []
for _ in range(N):
    x = int(input())
    if x == 0 and len(heap):
        print(heapq.heappop(heap)[1])
    elif x == 0 and len(heap) == 0:
        print(0)
    else:
        heapq.heappush(heap, (abs(x), x))
