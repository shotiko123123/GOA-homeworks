#2) შექმენით ფუნქცია რომელიც მიიღებს რიცხვების სიას და დაბრუნებს მხოლოდ ლუწების ჯამს.
def word(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

list = [1, 2, 3, 4, 5, 6,]
