def get_rate(num):
    if num == 6:
        return 1
    elif num == 5:
        return 2
    elif num == 4:
        return 3
    elif num == 3:
        return 4
    elif num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    cnt = 0
    cnt_zero = 0
    for lotto in lottos:
        for win_num in win_nums:
            if lotto == win_num:
                cnt += 1
        if lotto == 0:
            cnt_zero += 1
    answer = [get_rate(cnt_zero+cnt), get_rate(cnt)]
    return answer