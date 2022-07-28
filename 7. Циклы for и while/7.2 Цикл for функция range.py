7.2 Цикл for: функция range. Шаг_7.

Последовательность чисел - 1: Даны два целых числа m и n (m <= n).
Напишите программу, которая выводит все числа от m до n включительно.


m = int(input())
n = int(input())

for _ in range(m, n + 1):
	print(m)
	m += 1

##############################################################
7.2 Цикл for: функция range. Шаг_8.

Последовательность чисел 2: Даны два целых числа m и n.
Напишите программу, которая выводит все числа от m до n включительно в порядке возрастания,
если m < n, или в порядке убывания в противном случае.

На вход программе подаются два целых числа m и n, каждое на отдельной строке.

Программа должна вывести числа в соответствии с условием задачи.


m = int(input())
n = int(input())

if m < n:
	for i in range(m, n + 1):
		print(i)
else:
	for i in range(m, n - 1, -1):
		print(i)

##############################################################
7.2 Цикл for: функция range. Шаг_9.

Последовательность чисел 3: Даны два целых числа m и n (m > n). Напишите программу, которая выводит
все нечетные числа от m до n включительно в порядке убывания.

На вход программе подаются два целых числа m и n, каждое на отдельной строке.

Программа должна вывести числа в соответствии с условием задачи.

Примечание. Попробуйте решить задачу двумя способами: с использованием условного оператора if
и без него.

# с использованием условного оператора if
m = int(input())
n = int(input())

for i in range(m, n - 1, -1):
	if i % 2 != 0:
		print(i)

# без него: pass

##############################################################
7.2 Цикл for: функция range. Шаг_10.

Последовательность чисел 4: Даны два натуральных числа m и n (m <= n).
Напишите программу, которая выводит все числа от m до n включительно удовлетворяющие хотя бы
одному из условий:
	- число кратно 17;
	- число оканчивается на 9;
	- число кратно 3 и 5 одновременно.

На вход программе подаются два натуральных числа m и n (m <= n), каждое на отдельной строке.

Программа должна вывести числа в соответствии с условием задачи.

Примечание. Если чисел удовлетворяющих условию нет, выводить ничего не надо.


m = int(input())
n = int(input())

for i in range(m, n + 1):
	if (i % 17 == 0) or (i % 10 == 9) or (i % 15 == 0):		# i % 3 == 0 and i % 5 == 0
		print(i)

##############################################################
7.2 Цикл for: функция range. Шаг_11.

Таблица умножения: Дано натуральное число n. Напишите программу, которая выводит таблицу умножения
на n.

На вход программе подается натуральное число.

Программа должна вывести таблицу умножения на введенное число.

Примечание. В качестве знака умножения используйте английскую букву 'x'.


n = int(input())

for i in range(1, 11):
	print(n, "x", i, "=", n * i)

