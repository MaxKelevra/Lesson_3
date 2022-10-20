def num_sum():
    s = 0
    while True:
        err = False
        in_list = input("введите число, нажмите 'q' для выхода: ").split()
        for num in in_list:
            if num.lower() == 'q':
                return s
            else:
                try:
                    s += int(num)
                except ValueError:
                    err = True
        if err:
            print("Введены некоректные данные!")
        print(f"Сумма чисел: {s}")
print(num_sum())
