import csv, pickle


class Subway:
    def __init__(self, name):
        self.name = name
        self.lines = {}
        self.stations = {}

    def save_lines(self):
        path = "../res/" + self.name + ".csv"
        with open(path, 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for station in reader:
                inf = [x.split(",") for x in station[1].split()]
                self.stations[station[0]] = inf
        for (key, values) in self.stations.items():
            for t in values:
                t[1]=int(t[1])


if __name__ == '__main__':
    sub = Subway("北京")
    sub.save_lines()
    for (key,value) in sub.stations.items():
        print(value)
