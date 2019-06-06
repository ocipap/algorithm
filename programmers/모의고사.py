def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    answer = {1: 0, 2: 0, 3: 0}
    max = 0
    res = []
    for i in range(0, len(answers)):
        cur = answers[i]
        if cur == p1[i % 5]:
            answer[1] += 1
        if cur == p2[i % 8]:
            answer[2] += 1
        if cur == p3[i % 10]:
            answer[3] += 1
    for k, v in answer.items():
        if max < v:
            res.clear()
            res.append(k)
            max = v
        elif max == v:
            res.append(k)

    return res
