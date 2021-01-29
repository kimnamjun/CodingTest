def solution(phone_book):
    phone_book = sorted(phone_book, key=lambda x: len(x))
    for idx, val in enumerate(phone_book):
        for pb in phone_book[:idx]:
            if val.startswith(pb):
                return False
    return True