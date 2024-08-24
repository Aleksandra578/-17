import random

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Удаление предмета
        5. Удаление ученика и его данных (оценок)
        6. Редактирование предметов в списке
        7. Редактирование ученика
        8. Редактирование оценок ученика
        9. Удаление ученика и его данных (оценок)
        10. Вывод информации по всем оценкам по определенному ученику
        11. Вывод среднего балла по каждому предмету по определенному ученику
        12. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удаление предмета')
        class_ = input('Введите предмет, который хотите удалить: ')
        if class_ in classes:
            classes.remove(class_)
            print(classes)
            print('Предмет удален')
        else:
            print('Данного предмета нет в списке')
    elif command == 5:
        print('5. Добавление предмета в список')
        new_class_i = input('Введите название нового предмета: ')
        if new_class_i in classes:
            print('Указанный предмет уже есть в списке')
        else:
            classes.append(new_class_i)
            print(f'Предмет добавлен в список: {classes}')
    elif command == 6:
        print('6. Редактирование предметов в списке')
        class_b = str(input('Введите предмет для редактирования: '))
        n_class = str(input('Введите новое название предмета: '))
        index = classes.index(class_b)
        for student_b in students_marks:
            students_marks[student_b][n_class] = students_marks[student_b][class_b]
            del students_marks[student_b][class_b]
        classes.remove(class_b)
        classes.insert(index, n_class)
        print(f'Предмет изменен на {n_class}')
    elif command == 7:
        print('7. Редактирование ученика')
        redact_name = input('Введите имя ученика для редактирования: ')
        redact_student = input('Введите новое имя: ')
        if redact_student in students:
            print('Указанный ученик уже существует')
        else:
            students.append(redact_student)
            students_marks[redact_student] = students_marks[redact_name]
            if redact_name in students_marks:
                del students_marks[redact_name]
                students.remove(redact_name)
            print(f'Имя студена изменено имя на: {redact_student}')
    elif command == 8:
        print('8. Редактирование оценок ученика')
        student_ed = input('Введите имя ученика: ')
        class_с = input('Введите предмет: ')
        print(f'У студента по имени {student_ed} по {class_с} следующие оценки  {students_marks[student_ed][class_с]}')
        mark_del = int(input('Введите оценку для редактирования: '))
        mark_new = int(input('Введите оценку на которую нужно изменить: '))
        if student_ed in students_marks.keys() and class_с in students_marks[student_ed].keys():
            nn = students_marks[student_ed][class_с]
            index_mark = nn.index(mark_del)
            nn.remove(mark_del)
            nn.insert(index_mark, mark_new)
            print(f''' Для студента по имени {student_ed} по {class_с} изменена оценка {mark_del}
            Текущие оценки у студента {student_ed} = {students_marks[student_ed][class_с]} ''')
            del nn
        else:
            print('Данный ученик или предмет отсутствует')
    elif command == 9:
        print('9. Удаление ученика и его данных (оценок)')
        student_k = input('Введите ученика, которого хотите удалить: ')
        if student_k in students_marks:
            del students_marks[student_k]
            print(students_marks)
        else:
            print('Указанного ученика нет в списке')
    elif command == 10:
        print('10. Вывод информации по всем оценкам по определенному ученику')
        studentt = input('Введите имя ученика: ')
        if studentt in students_marks.keys():
            for classes_d, marks in students_marks[studentt].items():
                print(f'{classes_d} - {students_marks[studentt][classes_d]}')
            print()
        else:
            print('Указанного ученика нет в списке')
    elif command == 11:
        print('11. Вывод среднего балла по каждому предмету по определенному ученику')
        student = input('Введите имя ученика: ')
        if student in students_marks.keys():
            for classes, marks in students_marks[student].items():
                # находим сумму оценок по предмету
                marks_sum = sum(marks)
                # находим количество оценок по предмету
                marks_count = len(marks)
                # выводим средний балл по предмету
                print(f'{classes} - {marks_sum // marks_count}')
        print()
    elif command == 12:
        print('12. Выход из программы')
        break