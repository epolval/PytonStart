"""Реализуйте абстракцию (набор функций) для работы с прямоугольниками, стороны которого всегда
параллельны осям. Прямоугольник может располагаться в любом месте координатной плоскости.
При такой постановке достаточно знать только три параметра для однозначного задания
прямоугольника на плоскости: координаты левой верхней точки, ширину и высоту. Зная их,
мы всегда можем построить прямоугольник одним способом.
      Y
      |
    4 |    точка   ширина
      |       *-------------
    3 |       |            |
      |       |            | высота
    2 |       |            |
      |       --------------
    1 |
      |
------|--------------------------- X
    0 |  1   2   3   4   5   6   7

Основной интерфейс:
make_rectangle() (конструктор) — создает прямоугольник. Принимает параметры: левую верхнюю точку,
ширину и высоту. Ширина и высота – положительные числа
Селекторы get_start_point(), get_width() и get_height()
contains_origin() — проверяет, принадлежит ли центр координат прямоугольнику.
То есть не лежит на границе прямоугольника, а находится внутри. Чтобы в этом убедиться,
достаточно проверить, что все вершины прямоугольника лежат в разных квадрантах.
Их можно высчитать в момент проверки

# Создание прямоугольника:
# p - левая верхняя точка
# 4 - ширина
# 5 - высота
#
# p    4
# -----------
# |         |
# |         | 5
# |         |
# -----------
"""

def make_decart_point(x, y):
    return {"x": x, "y": y}


def get_x(point):
    return point["x"]


def get_y(point):
    return point["y"]


def get_quadrant(point):
    x = get_x(point)
    y = get_y(point)
    if x > 0 and y > 0:
        return 1
    if x < 0 < y:
        return 2
    if x < 0 and y < 0:
        return 3
    if y < 0 < x:
        return 4
    return None

def make_rectangle(p, w, h):
    p1 = p
    p2 = {"x": get_x(p) + w, "y": get_y(p)}
    p3 = {"x": get_x(p), "y": get_y(p) - h}
    p4 = {"x": get_x(p) + w, "y": get_y(p) - h}
    return {"p1": p1, "p2": p2, "p3": p3, "p4": p4}


def get_start_point(rectangle):
    return rectangle["p1"]


def get_width(rectangle):
    return get_x(rectangle["p2"]) - get_x(rectangle["p1"])


def get_height(rectangle):
    return get_y(rectangle["p1"]) - get_y(rectangle["p3"])


def contains_origin(rectangle):
    cond1 = get_quadrant(rectangle["p1"]) == 2
    cond2 = get_quadrant(rectangle["p2"]) == 1
    cond3 = get_quadrant(rectangle["p3"]) == 3
    cond4 = get_quadrant(rectangle["p4"]) == 4
    print(cond1 and cond2 and cond3 and cond4)
    return cond1 and cond2 and cond3 and cond4





p = make_decart_point(0, 1)
rectangle = make_rectangle(p, 4, 5)

contains_origin(rectangle)  # False

rectangle2 = make_rectangle(make_decart_point(-4, 3), 5, 4)
contains_origin(rectangle2)  # True

"""Подсказки
Квадрант плоскости — любая из четырех областей или углов, на которые плоскость 
делится двумя взаимно перпендикулярными прямыми, принятыми в качестве осей координат
Для определения квадранта, в которой лежит точка, используйте функцию get_quadrant():"""

point_1 = make_decart_point(2, 3)
point_2 = make_decart_point(-2, -3)
get_quadrant(point_1)  # 1
get_quadrant(point_2)  # 3