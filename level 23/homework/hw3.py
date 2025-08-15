# # #დავალება 3:
# # რობოტმა უნდა დაითვალოს, რამდენჯერ სცადე სწორი სიტყვის შეყვანა.
# # ანუ ყოველ ჯერზე, როცა სწორი სიტყვა უთხარი, უნდა დაიმახსოვროს და უთხრას ბოლოს რიცხვი.
count = 0
cvladi = 'saba', 'andria','nika','shotiko','gio'
for i in range(5):
    word = input('გამოიცანი სახელები: ')
    if word in cvladi:
        count += 1
        print('სწორია')
        
    else:
        print('არასწორია')
print(count)