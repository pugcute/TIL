import sys
sys.stdin = open('input.txt')

'''
def search(words, text):
    words_len = len(words)
    words_idx = 0
    text_idx = 0
    cnt = 0
    while words_idx < words_len and text_idx < text_len:
        if words[words_idx] != text[text_idx]:
            text_idx = text_idx-words_idx
            words_idx = -1
        text_idx += 1
        words_idx += 1
        if words_idx == words_len:
            cnt += 1
            text_idx = text_idx-words_idx+1
            words_idx = 0

    return cnt
'''
# 50점, 시간복잡도일듯



N = int(input())
text_len = int(input())
text = input()
'''
words = ''
for i in range(2*N+1):
    if i % 2 == 0:
        words += 'I'
    else:
        words += 'O'
print(search(words, text))
'''
# 50점

cnt = 0
pattern_cnt = 0
i = 1

while i < text_len-1:
    if text[i-1] == 'I' and text[i] == 'O' and text[i+1] == 'I':
        pattern_cnt += 1
        if pattern_cnt == N:
            pattern_cnt -= 1
            cnt += 1
        i += 1
    else:
        pattern_cnt = 0
    i += 1
print(cnt)
