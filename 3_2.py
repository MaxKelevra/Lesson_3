name = input("Введите ваше имя: ")
surname = input("Введите фамилию: ")
city = input("Ваш город: ")
mail = input("Ваш email: ")
tel = input("Ващ телефон: ")
def user_data(name, surname, city, mail, tel):

    return " ".join([name , surname, city, mail, tel])
print(user_data(name, surname, city, mail, tel))