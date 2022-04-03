import sys
import heapq
sys.stdin = open('input.txt')

N = int(input())
heap = []
for i in range(N):
    x = int(input())
    if x == 0 and len(heap) > 0:
        print(heapq.heappop(heap))
    elif x == 0 and len(heap) == 0:
        print(0)
    else:
        heapq.heappush(heap, x)
