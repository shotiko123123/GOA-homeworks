# #დავალება 5:
# შეიყვანე სიტყვა და რობოტმა უნდა დათვალოს რამდენი ხმოვანია და რამდენი თანხმოვანი აქვს მას.
# გაიმეორებს ამას მანამ, სანამ არ შეიყვან სწორ სიტყვას.

#  ანუ რობოტს ეუბნები სიტყვას → ის გეუბნება:

# "ამ სიტყვაში არის 3 ხმოვანი და 4 თანხმოვანი"

# და გთხოვს ახალს, სანამ სწორ სიტყვას არ ეტყვი

xmovani = 'აეიოუ'

while True:
    xmovani_count = 0
    tanxmovani_count = 0
    word = input('შეიყვანე სიტყვა: ')
    for i in range(len(word)):
        if word[i] in xmovani:
            xmovani_count += 1
        else:
            tanxmovani_count += 1
    print(xmovani_count, 'xmovania')
    print(tanxmovani_count, 'tanxmovania')
    if xmovani_count == 0:
        print('სწოი სიტყვაა')
        break
    list = [1,2,3]
