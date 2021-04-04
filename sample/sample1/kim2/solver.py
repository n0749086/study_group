def solve(question):
    answer = 0
    l = question.split("+")
    for elem in l:
        answer += int(elem)
    return answer
