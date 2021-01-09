def solution(phone_book):
    answer = True
    for i in range(len(phone_book)):
        for j in range(len(phone_book)):
            if phone_book[i] in phone_book[j] and i != j:
                if phone_book[j].find(phone_book[i]) == 0:        # 이거 대신 phone_book[j].startswith(p1): 을 이용할 수 있다. 
                    return False                                   # zip을 이용한 비교도 좋을 것 같다. zip(phone_book, phone_book[1:]) : 으로 앞뒤 비교가능 

    return answer


""'
def solution(phoneBook):
    phoneBook = sorted(phoneBook)                                   # 원본은 유지하고 새로운 list을 주는 b = sorted(a)
                                                                    # 원본을 정렬하는 a.sort(), return 은 None
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True
