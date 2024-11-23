"""Отрезок — еще один графический примитив. В коде описывается парой точек,
одна из которых — начало отрезка, другая — конец. Обычный отрезок не имеет направления,
поэтому вы сами можете выбирать, какую точку считать началом, а какую - концом.
В этом задании подразумевается, что вы уже понимаете принцип построения абстракции.
Вы способны самостоятельно принять решение о том, как она будет реализована.
Сделать это можно разными способами и нет одного правильного.
src/segments.py
Реализуйте указанные ниже функции:
make_segment() — принимает на вход две точки и возвращает отрезок
get_mid_point_of_segment() — принимает на вход отрезок и возвращает точку,
которая находится на середине отрезка
get_begin_point() — принимает на вход отрезок и возвращает точку начала отрезка
get_end_point() — принимает на вход отрезок и возвращает точку конца отрезка
Представление отрезка вы должны придумать сами.
Для создания точек используйте функцию make_decart_point()"""

def make_decart_point(x, y):
    print({'x': x, 'y': y})
    return {'x': x, 'y': y}


def make_segment(p1:dict, p2:dict) -> dict:
    print({'start': p1, 'end': p2})
    return {'start': p1, 'end': p2}


def get_mid_point_of_segment(segment):
    p1 = segment['start']
    p2 = segment['end']
    new_x = (p1['x'] + p2['x']) / 2
    new_y = (p1['y'] + p2['y']) / 2
    print({'x': new_x, 'y': new_y})
    return {'x': new_x, 'y': new_y}


def get_begin_point(segment):
    print(segment['start'])
    return segment['start']


def get_end_point(segment):
    print(segment['end'])
    return segment['end']


segment = make_segment(make_decart_point(3, 2), make_decart_point(0, 0))
# В примерах ниже возвращаются точки с координатами (x, y)
get_begin_point(segment)  # {'x': 3, 'y': 2}
get_end_point(segment)  # {'x': 0, 'y': 0}
get_mid_point_of_segment(segment)  # {'x': 1.5, 'y': 1}



