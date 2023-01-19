import xlrd

def getData(filename, _course, institution): 
    book = xlrd.open_workbook(filename)
    sheet = book.sheet_by_index(0)
    countLessonInDayOfWeek = []
    day = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    count = 1

    # Нахождение количества занятий в каждый день недели
    for row in range(4, sheet.nrows):
        
        dayOfWeek = sheet.cell_value(rowx=row, colx=0)
        time = sheet.cell_value(rowx=row, colx=1)

        if (time != ""):
            if (dayOfWeek != ""):
                countLessonInDayOfWeek.append(count)
                count = 1
            else:
                count += 1

    countLessonInDayOfWeek.append(count)

    result = []

    # Перебор всех столбцов
    for col in range(2, sheet.ncols, 3):
        _speciality = sheet.cell_value(rowx=1, colx=col)
        _group = sheet.cell_value(rowx=2, colx=col)
        startDayOfWeekRow = 3

        # Перебор всех строк 
        for dayOfWeek in range(len(countLessonInDayOfWeek)):
            for countLesson in range(countLessonInDayOfWeek[dayOfWeek]):
                lesson = []
                row = startDayOfWeekRow + countLesson

                _discepline = sheet.cell_value(rowx=row, colx=col)
                _teacher = sheet.cell_value(rowx=row, colx=col+1)
                _cabinet = sheet.cell_value(rowx=row, colx=col+2)
                _day = day[dayOfWeek]
                _numberOfPair = countLesson + 1
                
                # Добавление данных о занятии
                lesson.append(institution)
                lesson.append(_course)
                lesson.append(_speciality)
                lesson.append(_group)
                lesson.append(_discepline)
                lesson.append(_teacher)
                lesson.append(_cabinet)
                lesson.append(_day)
                lesson.append(_numberOfPair)

                result.append(lesson)
            startDayOfWeekRow += countLessonInDayOfWeek[dayOfWeek]

    for col in range(len(result)):
        print(result[col])