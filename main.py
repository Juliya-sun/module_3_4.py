# def test_func(*params):
#     print('Тип:', type(params))
#     print('Аргумент:', params)
#
# test_func(1,2,3,4)

# def summator(*values):
#     s = 0
#     for i in values:
#         s += i
#     return s
#
#
# print(summator(1,2,3,4))
#
# def summator(txt, *values, type='summ'):
#     s = 0
#     for i in values:
#         s += i
#     return f'{txt}{s}{type}'
#
#
# print(summator('Сумма чисел:', 2,3,4))
#
# def info(value, *types, name_autor='Den', **values):
#     print('Тип:', type(values))
#     print('Аргумент:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
#
#
# info('пример использования параметров всех типов', 1, 2, 3, 4, name='Denis', course='Python')


def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if (root_word.lower() in word.lower() or
            word.lower() in root_word.lower()):
                same_words.append(word)

    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)


# Вывод на консоль:
# ['richiest', 'orichalcum', 'richies']
# ['Able', 'Disable']





