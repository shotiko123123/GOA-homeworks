age = int(input("enter your age: "))
student_card = input("do you got student card? (yes/no): ")

if age < 18 or student_card == "yes":
    print("დანაზოგი გაქვს!")
elif age >= 60 and student_card != "yes":
    print("პენსიონერის ფასდაკლება გაქ!")
else:
    print("ფასდაკლება არ გეკუთვნის.")