from fractions import Fraction
y, w = list(map(int, input().split()))
die = [1,2,3,4,5,6]
if y > w:
    ind = die.index(y)
else:
    ind = die.index(w)
difference = 6 - ind


probability = Fraction(difference,6)
if probability == 0:
    print("0/1")
elif probability == 1:
    print("1/1")
else:
    print(probability)
