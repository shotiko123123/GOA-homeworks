#3)შექმენით ფუნქცია რომელიც აბრუნებს სიაში უმაღლეს რიცხვს.
def number(numbers):
    if not numbers:
        return None
    max = numbers[0]
    for num in numbers:
        if num > max:
            max = num
    return max

numbers = [10, 25, 7, 42, 3]
print("ყველაზე დიდი რიცხვი:",number(numbers))