def solution(answers):
    answer = [0,0,0]
    stu0 = [ 1, 2, 3, 4, 5]
    stu1 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu2 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    temp = []
    for idx, num in enumerate(answers):     # enumerate 을 효율적으로 사용하자!
        if stu0[idx%5] == num:
            answer[0] += 1
        if stu1[idx%8] == num:
            answer[1] += 1
        if stu2[idx%10] == num:
            answer[2] += 1


    for idx, num in enumerate(answer):
        if num == max(answer):
            temp.append(idx+1)
    return temp
