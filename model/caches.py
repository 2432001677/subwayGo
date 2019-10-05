import csv
import os
import pickle


class Station:
    def __init__(self, subway, key, inf):
        self.subway = subway
        self.name = key
        self.inf = {x[0]: x[1] for x in inf}
        self.routes = None

    def __contains__(self, item):
        for line in self.inf.keys():
            if line == item:
                return True
        return False

    def _is_circle(self, route1, route2) -> bool:
        if not self.routes:
            with open("../res/" + self.subway + "/lines.pk", 'rb') as f:
                self.routes = pickle.load(f)
        route1 = [x[0] for x in self.routes[route1]]
        route2 = [x[0] for x in reversed(self.routes[route2])]
        return route1 == route2

    def __sub__(self, other):
        value = 9999
        min_line = None
        self.inf: dict
        for line in self.inf.keys():
            if line in other:
                t = self.inf[line][0] - other.inf[line][0]
                t = t if t > 0 else -t
                if t < value:
                    value = t
                    min_line = line
                elif t == value and self._is_circle(min_line, line):  # 解决要命的特殊情况——环路问题
                    temp = len(self.routes[line]) - value
                    if value <= temp:
                        if self.inf[line][0] - other.inf[line][0] < 0:
                            min_line = line
                    else:
                        value = temp
                        if self.inf[line][0] - other.inf[line][0] > 0:
                            min_line = line
        return value


class SubwayCache:
    def __init__(self, name):
        self.name = name
        self.lines = {}
        self.stations = {}
        self._station = []
        self._generate_caches()

    def get_station(self, name) -> Station:  # 得到站点对象
        for s in self._station:
            if s.name == name:
                return s
        return None

    def get_line_stations(self, line) -> list:  # 返回整条线路的站点信息
        return self.lines[line]

    def _generate_caches(self):
        path = "../res/" + self.name
        if not os.path.exists(path):
            os.mkdir(path)
        self._load_stations()
        self._load_lines()

    def _load_stations(self):
        path = "../res/" + self.name + "/stations.pk"
        if not os.path.exists(path):
            self._generate_stations(path)
        else:
            with open(path, 'rb') as f:
                self.stations = pickle.load(f)
        self.stations: dict[str:tuple]
        for (key, inf) in self.stations.items():
            self._station.append(Station(self.name, key, inf))

    def _load_lines(self):
        path = "../res/" + self.name + "/lines.pk"
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
                t: list[str, tuple:int, int]
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


if __name__ == '__main__':
    sub = SubwayCache("北京")
    s = sub.get_station("西直门")
    print(s.inf)
    t = sub.get_station("安定门")
    print(t.inf)
    print(s - t)
