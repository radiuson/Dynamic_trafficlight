def init_point_data():
    f = open('RoadKnotPosition.txt')
    line_list = f.readlines()
    for line in line_list:
        name, x, y = line.split()
        exec(name + "= RoadKnot(" + x + "," + y + ")")
        exec(name + ".print_self()")
        


class RoadKnot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def print_self(self):
        print(self.x, self.y, "yes")


if __name__ == "__main__":
    print("running")
    init_point_data()
