#4) მომხმარებელს შემოატანინეთ ორი რიცხვი და დაბეჭდეთ უფრო მაღალი რიცხვი 
num1 = int(input('Enter Number'))
num2 = int(input('Enter Number'))

if num1 > num2:
    print('უფრო მაღალი')
elif num2 > num1:
    print('უფორ დაბალი')
else:
    print('ტოლია')