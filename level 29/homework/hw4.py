#4) შექმენით ფუნქცია, რომელიც იღებს წინადადებას, და მასში space-ების მაგივრად სიტყვებს შორის ჩასვამს ტირეს("-"). 
# საბოლოოდ კი აბრუნებს მას

def letter(x):
    words = x.split()
    m = '-'.join(words)
    return m
s = input('Enter letters: ')
print(letter(s))