import sys
from collections import deque
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    commands = list(input())
    N = int(input())
    numbers = input()
    numbers = list(map(int, numbers))


