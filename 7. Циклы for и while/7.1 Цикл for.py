7.1 Цикл for. Шаг_2.

Python is awesome: Напишите программу, которая выводит текс «Python is awesome!» (без кавычек) 10 раз, каждый на отдельной строке.


for i in range(10):
	print("Python is awesome!")

##############################################################
7.1 Цикл for. Шаг_3.

Повторяй за мной - 1: Дано предложение и количество раз которое его надо повторить. Напишите программу, которая повторяет данное предложение нужное количество раз.

В первой строке записано текстовое предложение, во второй — количество повторений.
Программа должна вывести указанное текстовое предложение нужное количество раз. Каждое повторение должно начинаться с новой строки.


s = input()
n = int(input())

for _ in range(n):
	print(s)

##############################################################
7.1 Цикл for. Шаг_4.

Последовательность символов: Напишите программу, которая использует ровно три цикла for для печати следующей последовательности символов:

AAA
AAA
AAA
AAA
AAA
AAA
BBBB
BBBB
BBBB
BBBB
BBBB
E
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
TTTTT
G


for _ in range(6):
	print("AAA")

for _ in range(5):
	print("BBBB")

print("E")

for _ in range(9):
	print("TTTTT")

print("G")

##############################################################
7.1 Цикл for. Шаг_5.

Звездный прямоугольник: На вход программе подается натуральное число n ∈ [1;20] — высота звездного прямоугольника.
Напишите программу, которая печатает звездный прямоугольник размерами n x 19.

Подсказка. Для печати звездной линии используйте умножение строки на число.


n = int(input())

for i in range(n):
	print("*" * 19)

##############################################################
7.1 Цикл for. Шаг_7.

Повторяй за мной - 2: Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9,
каждая с указанной строкой текста.


s = input()

for i in range(10):
	print(i, s)

##############################################################
7.1 Цикл for. Шаг_8.

Квадрат числа: На вход программе подается натуральное число n.
Напишите программу, которая для каждого из чисел от 0 до n (включительно) выводит фразу: «Квадрат числа [число] равен [число]»
(без кавычек).


n = int(input())

for i in range(n + 1):
	print("Квадрат числа", i, "равен", i ** 2)

##############################################################
7.1 Цикл for. Шаг_9.

Звездный треугольник: На вход программе подается натуральное число n, (n >= 2)– катет прямоугольного равнобедренного треугольника.
Напишите программу, которая выводит звездный треугольник в соответствии с примером:

Input 1:	Output 1:
3			***
			**
			*

Input 2:	Output 2:
11			***********
			**********
			*********
			********
			*******
			******
			*****
			****
			***
			**
			*


n = int(input())

for i in range(n):
    print('*' * n)    # print('*' * (n - i))
    n = n - 1

##############################################################
7.1 Цикл for. Шаг_10.

Популяция: На вход программе подается три натуральных числа m, p, n.

	m: стартовое количество организмов;
	p: среднесуточное увеличение в %;
	n: количество дней для размножения. 

Напишите программу, которая предсказывает размер популяции организмов.
Программа должна выводить размер популяции в каждый день, начиная с 1 и заканчивая n-м днем.

Программа должна вывести текст в соответствии с условием задачи.

Input 1:	Output 1:
10			1 10.0
50			2 15.0
6			3 22.5
			4 33.75
			5 50.625
			6 75.9375

Input 2:	Output 2:
100			1 100
25
1


m = int(input())
p = int(input())
n = int(input())

# v.1
for i in range(n):
        print(i + 1, m)
        m = m + m * (p / 100)


# v.2 comments
"""
    или # range(1, n + 1)
    можно еще записать как:
        m = m * (1 + p/100) или m *= 1 + p / 100

    Тогда значение справа не зависит от m,
    его вообще можно рассчитать раз перед циклом:
        factor = 1 + p / 100
    а в цикле делать:
        m *= factor

    factor = 1 + p / 100
    for i in range(1, n + 1):
        print(i, m)
        m *= factor
"""

