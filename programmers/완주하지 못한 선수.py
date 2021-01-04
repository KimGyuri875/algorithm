def solution(participant, completion):
    answer = ''
    a = {}
    for i in participant:
        if a.get(i) == None:
            a[i]=1
        else:
            a[i]+=1
        #result[a] = result.get(a, 0) + 1 으로 수정가능

    for i in completion:
        a[i]-=1

    for i in a.keys():
        if a[i] != 0:
            print(i)
            return i

"""
Counter를 이용하는 방법

import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
"""
