age = int(input('Enter Your age: '))
clock = int(input('Enter Clock: '))

if age < 18 and clock > 22:
    print('its time to sleep')
elif age > 60 and clock > 21:
    print('better if you sleep')
else:
    print('you can do anything')