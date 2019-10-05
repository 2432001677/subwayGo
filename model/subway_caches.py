import csv
import os
import pickle

from model.stations import Station


class SubwayCache:
    def __init__(self, name):
        # 地铁系统名字
        name: str
        self.name = name

        '''
        所有地铁线dict
        键为线路名
        值为线路下的站点列表
        每个站点为一个元组(站点名,坐标,开通状态)
        '''
        self.lines: dict[str:list[tuple[str, int, int]]]
        self.lines = {}

        '''
        所有站点
        字典类型,key为站点名字,value为一个列表
        列表嵌套列表表示同一站的不同线路
        每条线路包含一个线路名,对应一个元组(坐标,开通状态)
        '''
        self.stations: dict[str:list[str, tuple[int, int]]]
        self.stations = {}

        # 所有站点
        self._station: Station
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
        path = os.getcwd() + "/res/" + self.name
        if not os.path.exists(path):
            os.mkdir(path)
        self._load_stations()
        self._load_lines()

    def _load_stations(self):
        path = os.getcwd() + "/res/" + self.name + "/stations.pk"
        if not os.path.exists(path):
            self._generate_stations(path)
        else:
            with open(path, 'rb') as f:
                self.stations = pickle.load(f)
        for (key, inf) in self.stations.items():
            self._station.append(Station(self.name, key, inf))

    def _load_lines(self):
        path = os.getcwd() + "/res/" + self.name + "/lines.pk"
        if not os.path.exists(path):
            self._generate_lines(path)
        else:
            with open(path, 'rb') as f:
                self.lines = pickle.load(f)

    def _generate_stations(self, path):
        with open(os.getcwd() + "/res/" + self.name + ".csv", 'r', encoding="utf-8") as f:
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
        os.remove(os.getcwd()+"/res/" + self.name + "/stations.pk")
        os.remove(os.getcwd()+"/res/" + self.name + "/lines.pk")


if __name__ == '__main__':
    sub = SubwayCache("北京")
    s = sub.get_station("西直门")
    print(s.inf)
    t = sub.get_station("安定门")
    print(t.inf)
    print(s - t)