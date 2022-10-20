word = input("Введите слово: ")
def int_func(word):
    print(word.title())
    return
print(int_func(word))
words = input("Введите строку со словами разделенными пробелом: ").split()
for w in words:
    res = int_func(w)
    if res:
        print(res, ' ')
