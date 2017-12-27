# Функции, которая генерирует словарь, которой мы передаем два списка
def createDict(k, v):
    res = {}
    if (type(k) != list):
        raise Exception('First_Argument_Not_List_Exception')
    if (type(v) != list):
        raise Exception('Second_Argument_Not_List_Exception')

    for i in range(len(k)):
        try:
            res.update({k[i]: v[i]})
        except IndexError:
            res.update({k[i]: None})
    return res


a = ['key1', 'key2', 'key3', 'key4']
b = [1, 2, 3]


def test(a, b, res):
    try:
        assert createDict(a, b) == res, "{}\nНЕ РАВНО\n{}".format(createDict(a, b), res)
        print('Тест пройден')
    except AssertionError as e:
        print(e)


test(a, b, {'key1': 1, 'key2': 2, 'key3': 3, 'key4': None})