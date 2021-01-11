import functools
def solution(numbers):
    def cmp(a, b):
        num1 = a+b
        num2 = b+a
        return 1 if num1> num2 else -1
        
    answer = ''
    num_str = []
    for i in numbers:
        num_str.append(str(i))
    n = sorted(num_str, key=functools.cmp_to_key(cmp),reverse=True)
    answer = str(int(''.join(n)))

    return answer
