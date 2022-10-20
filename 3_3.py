def my_func(arg_1 , arg_2, arg_3):
    if arg_1 >= arg_3 and arg_2 >= arg_3:
        return arg_1 + arg_2
    elif arg_1 > arg_2 and arg_1 < arg_3:
        return arg_1 + arg_3
    else:
        return arg_2 + arg_3
print(f'Результат: {my_func(int(input("Аргумент № 1: ")), int(input("Аргумент № 2: ")), int(input("Аргумент №3: ")))}')
