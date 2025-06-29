#შეიყვანე ტექსტი და დაბეჭდე ბოლო სიმბოლო ინდექსის მეშვეობით (არა სლაისინგით და არა უარყოფითი ინდექსით).
#მაგ: "hello" → `o` (მოძებნე `len(text) - 1` ინდექსით)

text = input("Enter Text: ")
if len(text) > 0:
    last_index = len(text) - 1
    print("Last Symbol:", text[last_index])
else:
    print("Text is Empty.")
