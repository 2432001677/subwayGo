import csv
import os
import pickle


class Subway:
    def __init__(self, name):
        self.name = name
        self.lines = {}
        self.stations = {}
        self._station = []
        self._generate_caches()

    def get_station(self, name):  # 得到站点对象
        for s in self._station:
            if s.name == name:
                return s
        return None

    def get_line_stations(self, line):  # 返回整条线路的站点信息
        return self.lines[line]

    def _generate_caches(self):
        self._load_stations()
        self._load_lines()

    def _load_stations(self):
        path = "../res/" + self.name + "_stations.pk"
        if not os.path.exists(path):
            self._generate_stations(path)
        else:
            with open(path, 'rb') as f:
                self.stations = pickle.load(f)
        self.stations: dict[str:tuple]
        for (key, inf) in self.stations.items():
            self._station.append(Station(key, inf))

    def _load_lines(self):
        path = "../res/" + self.name + "_lines.pk"
        if not os.path.exists(path):
            self._generate_lines(path)
        else:
            with open(path, 'rb') as f:
                self.lines = pickle.load(f)

    def _generate_stations(self, path):
        with open("../res/" + self.name + ".csv", 'r', encoding="utf-8") as f:
            reader = csv.reader(f)
            for station in reader:
                inf = [x.split(",") for x in station[1].split()]
                self.stations[station[0]] = inf
        for (key, line) in self.stations.items():
            for i, t in enumerate(line):
                line[i] = [t[0], (int(t[1]), 1 if t[2] == "是" else 0)]

        with open(path, 'wb+') as f:
            pickle.dump(self.stations, f, )

    def _generate_lines(self, path):
        all_lines = {}
        for (key, line) in self.stations.items():
            key: str
            line: list[list[str, tuple[int, int]]]
            for i, t in enumerate(line):
                t: list[str, tuple[int, int]]
                if t[0] not in all_lines:
                    all_lines[t[0]] = [(key, t[1][0], t[1][1])]
                else:
                    all_lines[t[0]].append((key, t[1][0], t[1][1]))
        for (line, station) in all_lines.items():
            self.lines[line] = sorted(station, key=lambda x: x[1])
        with open(path, 'wb+') as f:
            pickle.dump(self.lines, f)

    def delete_cache(self):
        os.remove("../res/" + self.name + "_stations.pk")
        os.remove("../res/" + self.name + "_lines.pk")


class Station:
    def __init__(self, key, inf):
        self.name = key
        self.inf = {x[0]: x[1] for x in inf}

    def __contains__(self, item):
        for line in self.inf.keys():
            if line == item:
                return True
        return False

    def __sub__(self, other):
        value = 9999
        self.inf: dict[str, tuple]
        for line in self.inf.keys():
            if line in other:
                t = self.inf[line][0] - other.inf[line][0]
                t = t if t > 0 else -t
                if t < value:
                    value = t
        return value


if __name__ == '__main__':
    sub = Subway("北京")
    s = sub.get_station("积水潭")
    print(s.inf)
    t = sub.get_station("西直门")
    print(t.inf)
    print(s - t)
