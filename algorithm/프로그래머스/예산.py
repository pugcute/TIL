def solution(d, budget):
    documents = d
    documents.sort()
    tmp = 0
    idx = 0
    while (tmp < budget) and (idx < len(documents)):
        tmp += documents[idx]
        idx += 1
        if tmp == budget:
            break
        elif tmp > budget:
            idx -= 1
            break
    answer = idx
    return answer