import sys

pika, commands = map(int, sys.stdin.readline().split())
pika_dict = {}
for i in range(1, pika+1):
    n = sys.stdin.readline().rstrip()
    pika_dict[n] = i
    pika_dict[i] = n
for j in range(commands):
    command = sys.stdin.readline().rstrip()
    try:
        command = int(command)
        print(pika_dict[command])
    except:
        print(pika_dict[command])
# try except로 값 검증하자....