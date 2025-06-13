#1)მომხმარებელს შემოატანინეთ 3 რიცხვი და გამოიტანეთ მაგ სამი რიცხვის ჯამი
num1 = int(input('Enter Number '))
num2 = int(input('Enter Number '))
num3 = int(input('Enter Number '))

print(num1 + num2 + num3)

#2)დაბეჭდეთ რიცხვები 10 - 1 მდე 

for i in range (10,0,-1):
    print(i)

#3)დაბეჭდეთ 1- 100 რიცხვი მხოლოდ კენტები

for i in range (1,101,2):
    print(i)

#4)დაბეჭდეთ ყველა რიცხვი რომელიც 3 ზე უნაშთოდ იყოფა 1- 100
for i in range(1, 101):
    if i % 3 == 0:
     print(i)

#5)იპოვეთ 1 - 100 რიცხვის ჯამი 

num = 0
for i in range(1,101):
   total += i

print('Total', num)