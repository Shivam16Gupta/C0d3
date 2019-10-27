a = int(input('Enter a number: '))

def fectorial(a):
if a < 0:
print('Invalid number. ')
elif a == 0:
print(a)
elif a == 1:
print(a)
else:
count = 1
for i in range(1, a+1):
count *= i
print(count)

fectorial(a)
