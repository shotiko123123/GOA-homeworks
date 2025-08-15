#5) შექმენით ფუნქცია, რომელსაც გადაეცემა სახელების სია. შექმენით ახალის სია, სადაც ჩაამატებთ გადმოცემული
#  სიიდან მხოლოდ იმ სახელებს, რომლებიც იწყება "N"-ზე`. საბოლოოდ დააბრუნეთ ეს სია

def li(list):
    names = []

    for name in list:
        if name.lower().startswith("n"):
            names.append(name)

    return names
names = ['Shotiko', 'Giorgi', 'Nika', 'Nino', 'luka']
result = li(names)
print(result)