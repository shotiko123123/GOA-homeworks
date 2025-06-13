ricxvi1 = float(input('Enter Number: '))
ricxvi2 = float(input('Enter Number: '))

if ricxvi1 > 0 or ricxvi2 <= 0:
    print('Both Number is possitvie')
elif (ricxvi1 > 0 and ricxvi2 <= 0) or (ricxvi1 <= 0 and ricxvi2 > 0):
    print('Only one nubmer is posstive')
else:
    print("Neither number is positive")