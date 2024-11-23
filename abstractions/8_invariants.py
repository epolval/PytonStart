"""Реализуйте абстракцию для работы с рациональными числами,
которая включает в себя следующие функции:
Конструктор make — принимает на вход числитель и знаменатель, возвращает дробь
Селектор get_numer — возвращает числитель
Селектор get_denom — возвращает знаменатель
Сложение add — складывает переданные дроби
Вычитание sub — находит разность между двумя дробями
Не забудьте реализовать нормализацию дробей удобным для вас способом.
Подсказки
Приведение дробей к единому знаменателю
Функция gcd из модуля math находит наибольший общий делитель двух чисел
Функция to_str возвращает строковое представление числа (используется для отладки)
Функция int преобразует значение к целому числу"""

import math
def normalize(numer, denom):
    mygcd = math.gcd(numer, denom)
    return {"numer": int(numer / mygcd), "denom": int(denom / mygcd)}

def make(numer, denom):
    return normalize(int(numer), int(denom))


def get_numer(rational):
    #print(f'numer: {rational["numer"]}')
    return rational["numer"]


def get_denom(rational):
    #print(f'denom: {rational["denom"]}')
    return rational["denom"]

def add(rat1, rat2):
    denom1 = get_denom(rat1)
    denom2 = get_denom(rat2)
    denom3 = math.lcm(denom1, denom2)
    numer3 = get_numer(rat1) * denom3 / denom1 + get_numer(rat2) * denom3 / denom2
    #print({"numer": numer3, "denom": denom3})
    return normalize(int(numer3), int(denom3))

def sub(rat1, rat2):
    denom1 = get_denom(rat1)
    denom2 = get_denom(rat2)
    denom3 = math.lcm(denom1, denom2)
    numer3 = get_numer(rat1) * denom3 / denom1 - get_numer(rat2) * denom3 / denom2
    #print({"numer": numer3, "denom": denom3})
    return normalize(int(numer3), int(denom3))


def to_str(rat):
    print(f"{get_numer(rat)}/{get_denom(rat)}")
    return f"{get_numer(rat)}/{get_denom(rat)}"

rat1 = make(3, 9)
get_numer(rat1)  # 1
get_denom(rat1)  # 3
rat2 = make(10, 3)
rat3 = add(rat1, rat2)
to_str(rat3)  # 11/3
rat4 = sub(rat1, rat2)
to_str(rat4)  # -3/1
