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
        self.search_system()

    def select_route_start(self, route_index):
        self.stations_start = self.routes_start.get_stations_name(route_index)

    def select_route_end(self, route_index):
        self.stations_end = self.routes_end.get_stations_name(route_index)

    def select_subway(self, subway_index):
        self.current_subway_cache = SubwayCache(self.subway_dirs[subway_index])
        self.routes_start = Route(self.current_subway_cache.lines)
        self.routes_end = Route(self.current_subway_cache.lines)
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


if __name__ == '__main__':
    sub = SubwayControl()
