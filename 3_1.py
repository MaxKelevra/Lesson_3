def div():
    try:
        num_1 = int(input("Введите делимое: "))
        num_2 = int(input("Введите делитель: "))
        res = num_1 / num_2

    except ValueError:
        return "Ошибка в значении"
    except ZeroDivisionError:
        return "Вы не можете использовать ноль в качестве делителя"
    return res


res = div()
print(res)
