"""Реализуйте функцию get_mid_point(), которая находит точку
посередине между двумя указанными точками:
Средняя точка вычисляется по формуле x = (x1 + x2) / 2 и y = (y1 + y2) / 2."""

def get_mid_point(p1: dict, p2: dict):
    x1 = p1['x']
    x2 = p2['x']
    y1 = p1['y']
    y2 = p2['y']
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    print({'x': x, 'y': y})
    return {'x': x, 'y': y}



point1 = {'x': 0, 'y': 0}
point2 = {'x': 4, 'y': 4}
get_mid_point(point1, point2)  # {'x': 2.0, 'y': 2.0}
