#შექმენით ფუნქცია, რომელიც მიიღებს წინადადებას და დაბეჭდავს მის თითოეულ სიტყვაში სიმბოლოების რაოდენობას(ცალ-ცალკე)
def letter(x):
    words = x.split()
    for i in words:
        print(i + ' ' + str(len(i)))
a = input('Enter Letter: ')
letter(a)