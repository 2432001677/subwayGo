import os
from model.route import Route
from model.subway_caches import SubwayCache


class SubwayControl:
    def __init__(self):
        self.current_subway_cache = None
        self.subway_dirs = []
        self.routes_start = None
        self.routes_end = None
        self.routes_list_start = []
        self.routes_list_end = []
        self.stations_start = None
        self.stations_end = None
        self.all_station = []
        self.all_station_obj = {}
        self.distance = {}
        self.search_system()

    def select_route_start(self, route_index):  # 获得当前线路下所有站点  列表
        self.stations_start = self.routes_start.get_stations_name(route_index)

    def select_route_end(self, route_index):
        self.stations_end = self.routes_end.get_stations_name(route_index)

    def select_subway(self, subway_index):
        self.current_subway_cache = SubwayCache(self.subway_dirs[subway_index])
        self.routes_start = Route(self.current_subway_cache.lines)
        self.routes_end = Route(self.current_subway_cache.lines)
        self.all_station = self.current_subway_cache.stations.keys()
        self.all_station_obj = {x.name: x for x in self.current_subway_cache.station_obj}
        self.select_route_start(0)
        self.select_route_end(0)

    def search_system(self):
        subways = []
        path = os.getcwd() + "/res/"
        for a, b, c in os.walk(path):
            for i in b:
                if os.path.exists(path + i + "/lines.pk") and os.path.exists(path + i + "/stations.pk"):
                    subways.append(i)
        self.subway_dirs = subways
        self.select_subway(0)

    def _find_shortest_station(self) -> str:
        min = 9999
        min_s = ""
        for s in self.all_station:
            if self.distance[s][1] == 0 and self.distance[s][0] < min:
                min_s = s
                min = self.distance[s][0]
        return min_s

    def _get_same_route(self):
        pass

    def best_path(self, start_station, end_station):
        res = []
        if not self.all_station_obj[start_station].is_open():
            res.append("起点未开通")
        if not self.all_station_obj[end_station].is_open():
            res.append("终点未开通")
        if len(res) > 0:
            return res
        start_obj = self.all_station_obj[start_station]
        path = {x: start_station for x in self.all_station}  # 记录路径
        self.distance = {x: [start_obj - self.all_station_obj[x], 0] for x in self.all_station}  # 记录离原点最短距离,以及是否被访问
        self.distance[start_station][1] = 1
        min_station = self._find_shortest_station()
        while min_station != "":
            for s in self.all_station:
                sub = self.all_station_obj[min_station] - self.all_station_obj[s]
                if sub + self.distance[min_station][0] < self.distance[s][0]:
                    self.distance[s][0] = sub + self.distance[min_station][0]
                    path[s] = min_station
            self.distance[min_station][1] = 1
            min_station = self._find_shortest_station()
        line = [end_station]
        while end_station != start_station:
            end_station = path[end_station]
            line.append(end_station)
        line = list(reversed(line))
        n = len(line) - 1
        for i in range(n):
            line[i] = self.all_station_obj[line[i]].get_past_stations(self.all_station_obj[line[i + 1]])
        del line[n]

        return line
