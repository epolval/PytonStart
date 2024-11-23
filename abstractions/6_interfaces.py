"""В этой задаче тесты написаны для отрезков, которые используют точки.
Ваша задача — реализовать интерфейсные функции для работы с точками.
Внутреннее представление точек должно быть основано на полярной системе координат,
хотя интерфейс предполагает работу с декартовой системой (снаружи).
Реализуйте интерфейсные функции точек:
make_point() — принимает на вход координаты и возвращает точку, уже реализован
Трансляция декартовых координат в полярные была описана в теории
Получить x можно по формуле radius * cos(angle)
Получить y можно по формуле radius * sin(angle)"""

import math
def make_point(x, y):
    return {
        "angle": math.atan2(y, x),
        "radius": math.sqrt((x ** 2) + (y ** 2)),
    }


def get_angle(point):
    return point['angle']


def get_radius(point):
    return point['radius']


def get_x(point):
    x = get_radius(point) * math.cos(get_angle(point))
    print(int(x))
    return int(x)

def get_y(point):
    y = get_radius(point) * math.sin(get_angle(point))
    print(int(y))
    return int(y)


x = 4
y = 8

# point хранит в себе данные в полярной системе координат
point = make_point(x, y)

# Здесь происходит преобразование из полярной в декартову
get_x(point)  # 4
get_y(point)  # 8

