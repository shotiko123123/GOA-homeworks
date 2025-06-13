asaki = int(input("Enter Your Age: "))
wona = float(input("Enter Your Weight: "))

if asaki < 10:
    if wona < 20:
        print("weight is low")
    elif 20 <= wona <= 40:
        print("weight is normal")
    else:
        print("weight is big")

elif 10 <= asaki <= 17:
    if wona < 40:
        print('weight is low')
    elif 40 <= wona <= 65:
        print('weight is normal')

else:
    if wona < 50:
        print("weight is low")
    elif 50 <= wona <= 90:
        print("weight is noramll")
    else:
        print("weight is big")