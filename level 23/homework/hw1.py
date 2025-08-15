
xmovani = 'aeiou'

while True:
    word = input('შეიყვანე სიტყვა: ')
    if word[0] not in xmovani and word[-1] not in xmovani:
        print('სწორი სიტყვა')
        break
    else:
        print('ცადე თავიდან')