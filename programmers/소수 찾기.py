import itertools
def solution(numbers):
    #소수 판별법 
    answer = []
    numbers = list(map(str, str(numbers)))
    nPr = []   
    def isPrime(a):
        if a < 2:
            return False      
        for i in range(2, a):
            if a % i == 0:  
                return False
        return True

    for i in range(1, len(numbers)+1):
        nPr += (map(''.join, itertools.permutations(numbers, i)))

    nPr = list(map(int, nPr))
    for i in nPr:
        if isPrime(i):
            answer.append(i)
    return len(set(answer))
