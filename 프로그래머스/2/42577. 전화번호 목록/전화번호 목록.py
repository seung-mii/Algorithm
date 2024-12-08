def solution(phone_book):
    phone_dict = {}
    for phone in phone_book:
        phone_dict[phone] = True
    
    for phone in phone_book:
        temp = ""
        for char in phone:
            temp += char

            if temp in phone_dict and temp != phone:
                return False

    return True