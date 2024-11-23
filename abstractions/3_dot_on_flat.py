"""Реализуйте функцию calculate_distance(), которая находит расстояние
между двумя точками на плоскости:"""


def calculate_distance(point1,point2):
    import math

    x1, y1 = point1
    x2, y2 = point2
    result =  math.sqrt(abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2)
    return result


if __name__ == '__main__':
    point1 = [0, 0]
    point2 = [3, 4]
    print(calculate_distance(point1,point2))
    print(calculate_distance(point2, point1))