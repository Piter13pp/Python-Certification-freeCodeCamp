def verify_card_number(number_str):
    number_str = number_str.replace("-", "").replace(" ", "")
    number_arr = text_to_number_array(number_str)
    
    number_arr = number_arr[::-1] 
    
    sum = 0
    for i, num in enumerate(number_arr): 
        if i % 2 == 1:
            num = num * 2
            if num > 9:
                num = num - 9
        sum = sum + num
    
    if sum % 10 == 0:
        return "VALID!"
    else:
        return "INVALID!"

def text_to_number_array(text):
    return [int(char) for char in text]

print(verify_card_number('453914889'))  # VALID
print(verify_card_number('4111-1111-1111-1111'))  # VALID
print(verify_card_number('453914881'))  # INVALID
print(verify_card_number('1234 5678 9012 3456'))  # INVALID