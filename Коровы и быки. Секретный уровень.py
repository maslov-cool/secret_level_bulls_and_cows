import random


attempt = 0
history = []
# в словаре хранятся коровы('cows' - значения) и быки (bulls: индексы):
dict_ = {'cows': [], 'bulls': []}


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
    for i in range(len(l2)):
        if l2[i] == l1[i]:
            bulls += 1
            if i not in dict_['bulls']:
                dict_['bulls'].append(i)
    for i in range(len(l2)):
        if l2[i] in l1:
            if l2[i] and l2[i] not in dict_['cows'] and i not in dict_['bulls']:
                cows += 1
                dict_['cows'].append(l2[i])
    return bulls, cows


def check(human_num_: int, bot_num_: int) -> bool:
    global dict_
    l1 = number_to_list(human_num_)
    l2 = number_to_list(bot_num_)
    # в процессе генерации мы генерируем только цифры, индексы которых не в dict_['bulls']
    if len(str(bot_num_)) == 4 and all(j in [l2[i] for i in range(len(l2)) if i not in dict_['bulls']]
                                       for j in dict_['cows']):
        return True
    return False


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
    bot_num = [i for i in str(human_num)]
    for i in range(len(bot_num)):
        if i:
            if i not in dict_['bulls']:
                bot_num[i] = str(random.randint(0, 9))
        else:
            if i not in dict_['bulls']:
                bot_num[i] = str(random.randint(1, 9))
    bot_num = int(''.join(bot_num))
    while not check(human_num, bot_num):
        bot_num = [i for i in str(human_num)]
        for i in range(len(bot_num)):
            if i not in dict_['bulls']:
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
    for i in dict_['cows']:
        if str(i) in str(human_num) and str(human_num).index(str(i)) == str(bot_num).index(str(i)):
            dict_['bulls'].append(i)
            del dict_['cows'][dict_['cows'].index(i)]
            
print('Поздравляю с победой!')



