def solution(n, lost, reserve):
    answer = 0
    set_lost = set(lost)
    set_reserve = set(reserve)
    final_lost = list(set_lost - set_reserve)
    final_reserve = list(set_reserve - set_lost)
    for i in range(1, n+1):
        if i not in final_lost:
            answer += 1
        else:
            if (i-1) in final_reserve and (i+1) in final_reserve:
                final_reserve.remove(i-1)
                answer += 1
            elif (i+1) in final_reserve:
                final_reserve.remove(i+1)
                answer += 1
            elif (i-1) in final_reserve:
                final_reserve.remove(i-1)
                answer += 1
    return answer