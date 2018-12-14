import numpy as np
import Draw_graph


def get_neighbor(c_list, now):
    knot = c_list[now]
    knot_path_list = []
    count = 0
    for p in knot:
        if p == 0:
            pass
        else:
            knot_path_list.append([now, count, p])
        count += 1
    return knot_path_list


def check_next(now_knot, sum_kpl, pre_list):  # 返回找到的当前点的下一点的列表，返回点索引与距离
    nkl = []
    p = 0
    while p < len(sum_kpl):
        if sum_kpl[p][0] == now_knot[0] and sum_kpl[p][1] not in pre_list:
            nkl.append([sum_kpl[p][1], sum_kpl[p][2]])
            sum_kpl.pop(p)
            p -= 1
        p += 1

    return nkl


def check_short(kpl):
    for p in kpl:
        for pp in kpl:
            if p[1] == pp[1] and p[0] == pp[0] and p[2] >= pp[2]:

            else:



def expand_self(now_knot, pre_knot_list, distance_list, sum_kpl, kpl):
    while True:
        distance = sum(distance_list)
        kpl.append([pre_knot_list.copy(), distance])
        next_knot_list = check_next(now_knot, sum_kpl, pre_knot_list)
        if next_knot_list:
            for next_knot in next_knot_list:
                pre_knot_list.append(next_knot[0])
                distance_list.append(next_knot[1])

                expand_self(next_knot, pre_knot_list, distance_list, sum_kpl, kpl)

        else:
            pre_knot_list.pop()
            distance_list.pop()
        now_knot = [pre_knot_list[-1], distance_list[-1]]
        if not pre_knot_list:
            return kpl


def make_path_list(p_list, c_list):
    sum_kpl = []
    for n in range(len(p_list)):
        for c in get_neighbor(c_list, n):
            sum_kpl.append(c)
    for knot in p_list:
        name, x, y, knot_index = knot

    return sum_kpl


if __name__ == '__main__':
    position_file_path = 'RoadKnotPosition'
    connection_file_path = 'knot_connection'
    connection_list, position_list = Draw_graph.init_point_data(position_file_path, connection_file_path)
    sum_knot_path_list = make_path_list(position_list, connection_list)
    knot_path_list = expand_self([0, 0], [0], [], sum_knot_path_list, [])
    print(connection_list)
    print(knot_path_list)
