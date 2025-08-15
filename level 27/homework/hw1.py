#შექმენით ფუნქცია, რომელსაც გადაეცემა სიმბოლოების სია. ფუნქციამ უნდა დააბრუნოს ეს სია პირველი და ბოლო ელემენტების გარეშე, გამოიყენეთ slicing-ი

def letter(list):
    return list[1:-1]



symbol = ['a', 'b', 'c', 'd']
reseult = letter(symbol)
print(reseult)