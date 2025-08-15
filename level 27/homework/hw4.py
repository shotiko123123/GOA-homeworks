#4) შექმენით ფუნქცია, რომელსაც გადაეცემა რიცხვების სია. გადაუარეთ ამ სიას for ციკლით და ჩაამატეთ მხოლოდ
# ლუწი რიცხვები ახალ სიაში. საბოლოოდ დააბრუნეთ ეს სია

def number(numbers):
    result = []
    for num in numbers:
        if num % 2 == 0:
            result.append(num)
    return result