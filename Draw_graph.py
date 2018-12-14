import matplotlib.pyplot as plt
import numpy as np


def init_point_data(p_file_path, c_file_path):  # 通过预先设置的表生成位置信息
    file_position = open(p_file_path)
    file_connection = open(c_file_path)
    connection_raw_list = []
    sequenced_index = []
    p_list = []
    position_file_list = file_position.readlines()
    for position_line in position_file_list:
        p_list.append(position_line.split())

    for knot in p_list:
        name, x, y, knot_index = knot
        sequenced_index.append(name)
        y = 50 - float(y)
        plt.plot([float(x)], [y], 'ro')
        plt.axis()

    connection_file_list = file_connection.readlines()
    for connection_line in connection_file_list:
        connection_raw_list.append(connection_line.split())

    c_list = np.zeros([len(p_list), len(p_list)])
    for connection in connection_raw_list:
        name1, x1, y1, knot_index1 = p_list[sequenced_index.index(connection[0])]
        name2, x2, y2, knot_index2 = p_list[sequenced_index.index(connection[1])]
        length = pow((pow((float(x1) - float(x2)), 2) + pow(float(y1) - float(y2), 2)), 0.5)
        c_list[int(knot_index1)][int(knot_index2)] = length
        c_list[int(knot_index2)][int(knot_index1)] = length

    return c_list, p_list


def traffic_light():
    pass


def generate_car(map_size):
    origin = (np.random.randint(1, map_size), np.random.randint(1, map_size))
    destination = (np.random.randint(1, map_size), np.random.randint(1, map_size))
    return origin, destination


def find_car_path():
    pass


class Car:
    def __init__(self, size):
        self.origin, self.destination = generate_car(map_size=size)


class RoadKnot:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_self(self):
        print(self.x, self.y, "yes")


if __name__ == '__main__':
    position_file_path = 'RoadKnotPosition'
    connection_file_path = 'knot_connection'
    connection_list, position_list = init_point_data(position_file_path, connection_file_path)
    print(position_list)
    print(connection_list)
