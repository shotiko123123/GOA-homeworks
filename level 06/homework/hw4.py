#მომხმარებელს შემოატანინეთ რიცხვი და თუ ის არის ლუწი და არის 10-ზე მეტი, ან ტოლია 7-ის, დაბეჭდეთ True
num1 = int(input('Enter Your Number '))

if (num1 % 2 == 0 and num1 > 10) or num1==7:
    print('True')
else:
    print(False)
