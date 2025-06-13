age = int(input('Enter Your Age: '))
heartbeat = int(input('Enter Your Heartbeat: '))

if age < 30 and heartbeat <140:
    print('შეგიძლიათ მეტი ივარჯიშოთ')

elif age >= 30 and heartbeat > 170:
    print('დასვენება გჭირდებათ')

else:
    print('აქტივობის დონე ნორმალურია')