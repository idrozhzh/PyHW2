while 1:
    age = int(input("Введите год рождения А.С Пушкина: "))
    if age == 1799:
        while 1:
            day = int(input("Введите день рождения: "))
            if day == 6:
                print("Верно!")
                break
            print("Неверный день!")
        break
    print("Неверно!")