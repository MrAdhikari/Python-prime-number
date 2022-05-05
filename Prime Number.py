x = int(input('check if prime?'))
a = 0
for i in range(1, x + 1):
    if a>2:
        print('this number is Composite')
        break
    if x % i == 0:
        a = a + 1

if (a == 2):
    print("The number is prime ")

#my first prject

