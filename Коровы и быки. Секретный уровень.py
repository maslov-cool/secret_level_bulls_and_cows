import random


attempt = 0
history = []
# в словаре хранятся коровы('cows' - значения) и быки (bulls: словарь -> индекс: значение):
dict_ = {'cows': [], 'bulls': {}}


def check_num(n):
    return True if str(n).isdigit() and 999 < int(n) < 10000 else False


def number_to_list(number: int) -> list:
    return [int(i) for i in str(number)]


def bulls_and_cows(list_human_num: list, list_bot_num: list) -> (int, int):
    global attempt, dict_
    attempt += 1
    bulls, cows = 0, 0
    l1 = list_human_num
    l2 = list_bot_num
    for k in range(len(l2)):
        if l2[k] == l1[k]:
            if k not in dict_['bulls'].keys():
                bulls += 1
                dict_['bulls'][k] = l1[k]
                if l2[k] in dict_['cows']:
                    del dict_['cows'][dict_['cows'].index(l1[k])]
    for j in dict_['bulls'].keys():
        l1[j] = ''
        l2[j] = ''
    k = 0
    while k != len(l2):
        if l2[k] != '' and l2[k] in l1:
            cows += 1
            dict_['cows'].append(l2[k])
            del l1[l1.index(l2[k])]
            del l2[k]
            k -= 1
        k += 1
    return bulls, cows


def check(bot_num_: int) -> bool:
    global dict_
    l = number_to_list(bot_num_)
    l = [l[q] for q in range(len(l)) if q not in dict_['bulls'].keys()]
    # в процессе генерации мы генерируем только цифры, индексы которых не в dict_['bulls'],
    # поэтому проверка только на коров
    for i in dict_['cows']:
        if i in l:
            del l[l.index(i)]
        else:
            return False
    return True


print("Здравствуйте, добро пожаловать в игру 'Коровы и быки. 'Секретный уровень'")

bot_num = random.randint(1000, 9999)
print('Компьютер загадал число, попробуйте его угадать')

human_num = input()
while not check_num(human_num):
    print('Некорректный ввод')
    human_num = input()
human_num = int(human_num)

bulls_cows = bulls_and_cows(number_to_list(human_num), number_to_list(bot_num))
history.append((attempt, *bulls_cows))
print(f'Количество быков: {bulls_cows[0]}')
print(f'Количество коров: {bulls_cows[1]}')

while bot_num != human_num:
    bot_num = [i for i in '0000']
    for i in dict_['bulls'].keys():
        bot_num[i] = str(dict_['bulls'][i])
    bot_num = int(''.join(bot_num))

    while not check(bot_num):
        bot_num = [i for i in str(bot_num)]
        for i in range(len(bot_num)):
            if i not in dict_['bulls'].keys():
                bot_num[i] = str(random.randint(0, 9))
        bot_num = int(''.join(bot_num))
    human_num = input()
    while not check_num(human_num):
        print('Некорректный ввод')
        human_num = input()
    human_num = int(human_num)

    bulls_cows = bulls_and_cows(number_to_list(human_num), number_to_list(bot_num))
    print(f'Количество быков: {bulls_cows[0]}')
    print(f'Количество коров: {bulls_cows[1]}')
            
print('Поздравляю с победой!')





