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
            dict_['bulls'].append(i)
            l1[i] = ''
            l2[i] = ''
    for i in range(len(l2)):
        if l2[i] and l2[i] in l1 and l2[i] != l1[i]:
            cows += 1
            dict_['cows'].append(l2[i])
            l1[l1.index(l2[i])] = ''
    return bulls, cows


def check(human_num_: int, bot_num_: int) -> bool:
    global dict_
    l1 = number_to_list(human_num_)
    l2 = number_to_list(bot_num_)
    if all(l1[i] == l2[i] for i in dict_['bulls']) and all(j in [l1[i] for i in range(len(l1))
                                                                 if i not in dict_['bulls']] for j in dict_['cows']):
        return True
    return False


print("Здравствуйте, добро пожаловать в игру 'Коровы и быки. 'Секретный уровень'")

bot_num = random.randint(1000, 9999)
print('Компьютер загадал число, попробуйте его угадать')

human_num = int(input())
while not check_num(human_num):
    print('Некорректный ввод')
    human_num = int(input())

bulls_cows = bulls_and_cows(number_to_list(human_num), number_to_list(bot_num))
history.append((attempt, *bulls_cows))
print(f'Количество быков: {bulls_cows[0]}')
print(f'Количество коров: {bulls_cows[1]}')

while bot_num != human_num:
    bot_num = [i for i in str(human_num)]
    for i in range(len(bot_num)):
        if i not in dict_['bulls']:
            bot_num[i] = str(random.randint(0, 9))
    bot_num = int(''.join(bot_num))
    while not check(human_num, bot_num):
        bot_num = [i for i in str(human_num)]
        for i in range(len(bot_num)):
            if i not in dict_['bulls']:
                bot_num[i] = str(random.randint(0, 9))
        bot_num = int(''.join(bot_num))
    human_num = int(input())

    while not check_num(human_num):
        print('Некорректный ввод')
        human_num = int(input())

    bulls_cows = bulls_and_cows(number_to_list(human_num), number_to_list(bot_num))
    print(f'Количество быков: {bulls_cows[0]}')
    print(f'Количество коров: {bulls_cows[1]}')

print('Поздравляю с победой!')


