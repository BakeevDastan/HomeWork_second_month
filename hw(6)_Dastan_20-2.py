import re
while True:
    print('1 - Считать имена и фамилии\n2 - Считать все емайлы\n3 - Считать названия файлов'
          '\n4 - Считать цвета\n5 - Выход ')
    select_item = int(input('Выберите пункт: '))
    if select_item == 1:
        with open("MOCK_DATA.txt", "r", encoding="utf-8") as file:
            content = file.read()
            with open("name.txt", 'w', encoding='utf-8') as names:
                name = re.findall(r"(?:[A-Z-'][a-z-']+\s)(?:[A-Za-z'-]*\s|[A-Za-z-'])", content)
                for i in name:
                    i = str(i)
                    names.write(i + '\n')
        print('Имена и фамилии посчитаны и сохранены в файл "name.txt"')
    elif select_item == 2:
        with open("emails.txt", 'w', encoding='utf-8') as emails:
            email = re.findall(r"(?:[A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(?:\.[A-Z|a-z]{2,})+", content)
            for i in email:
                i = str(i)
                emails.write(i+'\n')
        print('Все почты посчитаны и сохранены в файл "emails.txt"')
    elif select_item == 3:
        with open("files.txt", 'w', encoding='utf-8') as files:
            file = re.findall(r'\s[A-Za-z]+\.[A-Za-z0-9]+', content)
            for i in file:
                i = str(i)
                files.write(i + '\n')
        print('Названия файлов посчитаны и сохранены в файл "file.txt"')
    elif select_item == 4:
        with open("colors.txt", 'w', encoding='utf-8') as colors:
            color = re.findall(r'#[a-z0-9]+', content)
            for i in color:
                colors.write(i + '\n')
        print('Цвета посчитаны и сохранены в файл "name.txt"')
    elif select_item == 5:
        print('Выход')
        break
    else:
        print('Введите правильное число от 1го до 5ти')









# **: У вас есть файл MOCK_DATA.txt, в котором 1000 строк с данными (Имя и Фамилия, емайл, название файла с расширением и код цвета)
#
# 1. Написать программу, где отображается меню с опциями: 1 - Считать имена и фамилии, 2 - Считать все емайлы, 3 - Считать названия файлов, 4 - Считать цвета, 5 - Выход
# 2. При выборе опции меню необходимо считать соответствующую информацию из файла с данными при помощи регулярных выражений и сохранить считанные данные в новый файл.
# 3. Если пользователь выбирает пункт в меню 1: считываются все имена и фамилии (1000 строк) и сохраняются в файл под названием names.txt. Если пользователь выбирает пункт в меню 2: считываются все емайлы (1000 строк) и сохраняются в файл под названием emails.txt и тд.
# 4. До тех пор пока пользователь не выбрал пункт 5 программа работает и предлагает опции меню.
# 5. При повторном выборе какого-то из пунктов меню, существующий файл с данными, например names.txt - полностью перезаписывается.