tanxmovani = set('ბგდვზთკლმნპჟრსტფქღყშჩცძწჭხჯჰ')

while True:
    sityva = input('Enter  word')
    if len (sityva) >= 2 and sityva[0] in tanxmovani and sityva[-1] in tanxmovani:
        print('არასწორია')
        break
    else:
        print('შეიყვანე თანხმოვანიანი სიტყვა')