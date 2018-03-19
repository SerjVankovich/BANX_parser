m = []

n = int(input('Введите количество значений массива - '))

for i in range(n):
	m.append(input('Введите значение ' + str(i + 1) + ' >> '))

print()

for name in m:
	print(name)
