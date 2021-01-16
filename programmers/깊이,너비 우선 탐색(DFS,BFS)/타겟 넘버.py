def solution(numbers, target):
    answer = 0
    level = len(numbers)
    def dfs(depth, total):
        if depth == level:
            if total == target:
                nonlocal answer
                answer += 1
        else:
            dfs(depth+1, total + numbers[depth])
            dfs(depth+1, total - numbers[depth])
    dfs(0, 0)
    return answer


"""
# 가지치기가 한눈에 잘보이는 코드 

def solution(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)
"""
