def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] in phone_book[j] and i != j:
                if phone_book[j].find(phone_book[i]) == 0:        # 이거 대신 phone_book[j].startswith(p1): 을 이용할 수 있다. 
                    return False

    return answer
