# разбивка заданной строки на отдельные слова и помещение их в отдельный список
# исключение TAB из слов и других символов для разбивки

# функция разделения строки на отдельные слова и помещение их в список
def stroka_naoborot(stroka_1):
    simvoli_razdelenia = {"", " ","\t"}  # можно внести любые символы, которыми необходимо разделять слова и которые исключаются
    spisok_slov = []  # создание списка для помещения туда отдельных слов строки
    slovo = ''  # создание переменной для помещения слова

    for i in stroka_1:  # цикл от первого символа строки до конца строки
        if i not in simvoli_razdelenia:  # если текущий символ в строке не равен множеству разделений,
            slovo += i  # то в переменную добавляется текущий символ
        else:
            if slovo in simvoli_razdelenia:  # проверка на первый символ разделения в строке и на множество пустот между словами
                slovo = ''
            else:  # конечное условие, если попадается пробел, то слово добавляется в сисок и обнуляется
                spisok_slov.append(slovo)
                slovo = ''
    if slovo != '':  # добавление последнего слова, если перед ним не стоит пробел
        spisok_slov.append(slovo)
        slovo = ''
    return spisok_slov


stroka = input("Введите строку: ")  # получение исходной строки
spisok = stroka_naoborot(stroka)

print(*spisok, sep="\n")

